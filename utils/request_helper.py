import allure
import logging
from pydantic import ValidationError, BaseModel
from typing import Type, TypeVar, Union, Dict
from playwright.sync_api import APIRequestContext, APIResponse, expect

# logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
T = TypeVar("T", bound=BaseModel)

def send_request(
        api_context: APIRequestContext, 
        method: str, 
        endpoint: str,
        status_code: int,
        extra_headers: Dict[str, str] = None,
        data: dict = None,
        form_data: dict = None, 
        schema: Type[T] = None)-> Union[APIResponse, T]:
    """
    Request sender with schema validation.

    :param api_context: Playwright APIRequestContext
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param endpoint: API endpoint
    :param status_code: Expected response status code
    :param schema: Pydantic schema for validation (Optional)
    :param kwargs: Additional arguments (json, params, headers, etc.)
    :return: APIResponse
    """
    with allure.step(f"Sending {method} request to {endpoint}"):
        logging.info(f"Request: {method} {endpoint} | Data: {data}")

        response: APIResponse = api_context.fetch(endpoint, method=method, data=data, form=form_data, headers=extra_headers)
        logging.info(f"Response: {response.status} | {response.text()}")    # log response before validation

        # Validate response status
        assert response.status == status_code, f"Expected status code: {status_code}, Actual: {response.status}"

        # Validate response schema if provided
        if schema:
            try:
                return schema.model_validate(response.json())
            except ValidationError as e:
                logging.error(f"Schema validation failed: {e}")
                allure.attach(response.text(), name="Invalid Response", attachment_type=allure.attachment_type.TEXT)
                raise AssertionError("Response schema validation failed!")

        return response