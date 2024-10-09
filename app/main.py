import os
import base64
import requests
import chainlit as cl
from chainlit.server import app
from chainlit.input_widget import Select, Switch
from fastapi.responses import JSONResponse
from app.app_logging import get_logger
from dotenv import load_dotenv

_ = load_dotenv()
logger = get_logger("app")

API_TIMEOUT = 60  # API Will Timeout in 60 Seconds
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
FASTAPI_URL = os.getenv("FASTAPI_URL")

messages = []
settings = None


@app.get("/health/live")
async def liveness_probe():
    return JSONResponse({"status": "live"})


@app.get("/health/ready")
async def readiness_probe():
    return JSONResponse({"status": "ready"})


@app.get("/health/startup")
async def startup_probe():
    return JSONResponse({"status": "live"})


@cl.on_chat_start
async def start():
    global settings
    global messages
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="OpenAI - Model",
                values=["gpt-3.5-turbo", "gpt-4o", "groq/llama3-70b-8192"],
                initial_index=0,
            ),
            Select(
                id="Language",
                label="Chat Language",
                values=["english", "marathi", "sanskrit"],
                initial_index=0,
            ),
            Switch(
                id="Clear Chat",
                label="Always Clears All Previous Messages when Page is Refreshed",
                initial=True,
            ),
        ]
    ).send()

    if settings["Clear Chat"] is True:
        # Start a Fresh Conversation
        messages = []


@cl.on_message
async def main(message: cl.Message):
    global settings
    global messages
    # Initialize the content list with the user's text message
    content_list = [{"type": "text", "text": message.content}]

    # Processing images if present
    images = [file for file in message.elements if "image" in file.mime]

    if images:
        for image in images:
            with open(image.path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")
                content_list.append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{image.mime.split('/')[-1]};base64,{base64_image}"
                        },
                    }
                )

    # Append the user's message with the combined text and image content
    messages.append({"role": "user", "content": content_list})

    # Prepare the payload
    payload = {
        "messages": messages,  # Messages now includes both text and image content
        "language": settings["Language"],
    }
    try:
        logger.info("Sending POST request to %s", FASTAPI_URL)
        response = requests.post(FASTAPI_URL, json=payload, timeout=API_TIMEOUT)
        response.raise_for_status()

        # Overwrite messages to keep it stateless
        messages = response.json()

        # Get the assistant's response content
        response_content = messages[-1].get("content", "No response found")
        logger.info("AI Response: %s...", str(response_content)[:700])

        # Send the response back to the client
        await cl.Message(content=response_content).send()

    except requests.Timeout:
        error_message = (
            f"Request to {FASTAPI_URL} timed out after {API_TIMEOUT} seconds"
        )
        logger.error(error_message)
        await cl.Message(content=error_message).send()

    except requests.RequestException as e:
        error_message = f"An error occurred while making the request: {str(e)}"
        logger.error(error_message)
        await cl.Message(content=error_message).send()

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logger.error(error_message)
        await cl.Message(content=error_message).send()
