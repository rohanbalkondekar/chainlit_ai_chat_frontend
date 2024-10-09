import os
import logging
from dotenv import load_dotenv

load_dotenv()


def get_logger(name):
    """
    Create and configure a logger instance.

    This function retrieves logging configuration from environment variables,
    creates a logger with the specified name, and sets up handlers for logging
    to both a file and the console based on the configuration.

    Parameters:
    name (str): The name of the logger. This is typically the module or
                class name where the logger is used.

    Returns:
    logging.Logger: A configured logger instance.
    """
    # Get configuration from environment variables
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # Log level (e.g., DEBUG, INFO)
    log_file = os.getenv("LOG_FILE", "")  # Optional log file path
    print_logs = os.getenv("PRINT_LOGS", "True").lower() == "true"  # Flag to print logs to console

    # Create logger
    logger = logging.getLogger(name)  # Create a logger with the specified name
    logger.setLevel(log_level)  # Set the logging level

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"  # Log message format
    )

    # Add file handler if LOG_FILE is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)  # Create a file handler
        file_handler.setFormatter(formatter)  # Set the formatter for the file handler
        logger.addHandler(file_handler)  # Add the file handler to the logger

    # Add stream handler if PRINT_LOGS is True
    if print_logs:
        stream_handler = logging.StreamHandler()  # Create a stream handler for console output
        stream_handler.setFormatter(formatter)  # Set the formatter for the stream handler
        logger.addHandler(stream_handler)  # Add the stream handler to the logger

    return logger  # Return the configured logger