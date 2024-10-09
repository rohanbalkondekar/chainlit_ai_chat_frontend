# README.md for the Project Directory

## Overview

Welcome to the project directory! This repository contains the implementation of a chat application built using Chainlit and FastAPI, along with the necessary components for managing interactive web applications. The project is structured to facilitate real-time communication between users and a backend service, providing features such as message handling, response generation, and health monitoring.

## Directory Structure

The project is organized into two main directories: `app` and `.chainlit`. Below is a brief overview of each directory and its contents.

### `app/`

The `app` directory contains the core implementation of the chat application.

- **main.py**: The main entry point of the chat application, implementing core functionality and health check endpoints.
- **app_logging/**: Utilities for structured logging within the application.
- **__init__.py**: Initializes the chat application and includes a message handler and event handler.
- **__pycache__/**: Contains compiled bytecode files managed automatically by Python.

### `.chainlit/`

The `.chainlit` directory facilitates the integration and management of Chainlit for building interactive applications.

- **app/**: Contains the main application files, including core logic and components.
- **config.py**: Manages configuration settings for the Chainlit application.
- **routes.py**: Defines the routing logic for the application.
- **static/**: Holds static assets such as images, stylesheets, and JavaScript files.
- **tests/**: Includes unit tests for Chainlit functionalities.

## Internal Dependencies

The application relies on several external libraries, which are managed in a virtual environment. Key dependencies include:

- **FastAPI**: A modern web framework for building APIs with Python.
- **Chainlit**: A library for creating interactive web applications.
- **Requests**: A simple HTTP library for making requests to the backend service.
- **Dotenv**: A library for loading environment variables from a `.env` file.

Ensure that these dependencies are installed in your virtual environment before running the application.

## Getting Started

To get started with the chat application, follow these steps:

1. **Set Up the Environment**: Ensure you have Python 3.10 or higher installed. Create a virtual environment and activate it.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**: Install the required packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Application**: Open the `config.py` file in the `.chainlit` directory and set the necessary configuration parameters, such as API keys and environment settings.

4. **Run the Application**: Start the chat application by executing the main script in the `app` directory.
   ```bash
   python app/main.py
   ```

5. **Access the Application**: Open your web browser and navigate to the specified URL (usually `http://localhost:8000` for the chat app and `http://localhost:5000` for the Chainlit app) to interact with the applications.

6. **Run Tests**: To ensure everything is working correctly, run the tests located in the `tests/` directory of the `.chainlit` module:
   ```bash
   pytest .chainlit/tests/
   ```

## Important Notes

- **Health Check Endpoints**: The chat application includes health check endpoints to monitor its status. You can access these endpoints to ensure the service is running correctly.
  
- **Logging Configuration**: The logging behavior can be customized using environment variables. Refer to the `app_logging` module for more details on how to configure logging.

## Contributing

We welcome contributions to this project! If you would like to add new features, improve existing functionalities, or enhance the documentation, please follow the contribution guidelines outlined in the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

For any questions or further assistance, please feel free to reach out to the development team. Happy coding!