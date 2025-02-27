import allure
import functools
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def step(description):
    """Custom step decorator for Allure reports and logging."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"STEP: {description}")  # Log step execution
            with allure.step(description):  # Allure step logging
                return func(*args, **kwargs)
        return wrapper
    return decorator