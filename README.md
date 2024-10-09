# Chainlit AI Chat Frontend (Demo Test)

## Overview
This is the frontend service for an AI chatbot. It provides a user interface for interacting with the chatbot using Chainlit.

## Run

Create a new virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

Set Python path:
```
export PYTHONPATH=$(pwd)
```

Install Requirements:
```
uv pip install -r requirements.txt
```

Run the app:
```
chainlit run app/main.py
```

## Access Points

- **Frontend (Chainlit)**: [http://localhost:8888/](http://localhost:8888/)

You can chat with the FAQ chatbot via the frontend UI at: [http://localhost:8888/](http://localhost:8888/)

## Directory Structure

```
.
├── app
│   ├── app_logging
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── __pycache__
│   ├── chainlit.md
│   ├── __init__.py
│   ├── main.py
│   └── __pycache__
├── chainlit.md
├── Dockerfile
├── README.md
└── requirements.txt
```

