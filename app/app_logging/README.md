# README.md for `app_logging`

## Overview

The `app_logging` module provides a structured approach to logging within a Python application. It includes utilities for creating and configuring loggers that can be used across different modules, ensuring consistent logging practices throughout the codebase.

## Structure

The `app_logging` directory contains the following files:

- `__init__.py`: This file defines the module and imports the `get_logger` function from the `logger` module. It specifies the public interface of the module, allowing users to access the `get_logger` function directly when importing `app_logging`.

- `logger.py`: This file contains the implementation of the `get_logger` function, which creates and configures a logger instance. The logger is customizable through environment variables, allowing developers to set the log level, log file path, and console output preferences. The logger is designed to provide a consistent format for log messages and can handle both file and console outputs.

## Usage

To use the logging functionality provided by this module, follow these steps:

1. **Import the Module**: Import the `app_logging` module in your Python script.
   ```python
   from app_logging import get_logger
   ```

2. **Get a Logger Instance**: Call the `get_logger` function to obtain a logger instance.
   ```python
   logger = get_logger()
   ```

3. **Log Messages**: Use the logger instance to log messages at various levels (e.g., debug, info, warning, error, critical).
   ```python
   logger.info("This is an informational message.")
   logger.error("This is an error message.")
   ```

## Internal Dependencies

- The `logger.py` file depends on the `dotenv` package for retrieving logging settings from environment variables. Ensure that the `dotenv` package is installed in your environment.

## Important Notes

- **Environment Variables**: The logging configuration can be customized using environment variables. Make sure to set the appropriate variables for log level, log file path, and console output preferences before running your application.
  
- **Consistent Logging**: Utilize the `get_logger` function across different modules to maintain a consistent logging format and behavior throughout your application.

## Conclusion

The `app_logging` module is designed to simplify logging in Python applications, providing a centralized way to manage loggers and their configurations. By following the usage guidelines, developers can ensure that their applications have a robust and consistent logging mechanism. For further questions or issues related to logging, please refer to the official Python logging documentation.