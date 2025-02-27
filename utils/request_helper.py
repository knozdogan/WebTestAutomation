import allure
import logging
import json
from pydantic import ValidationError, BaseModel
from playwright.sync_api import APIRequestContext, APIResponse, expect

# logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def send_request(
        api_context: APIRequestContext, 
        method: str, 
        endpoint: str, 
        status_code: int, 
        schema: BaseModel = None, **kwargs)-> APIResponse:
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
        logging.info(f"Request: {method} {endpoint} | Data: {kwargs.get('json', '')}")

        response: APIResponse = api_context.fetch(endpoint, method=method, **kwargs)
        logging.info(f"Response: {response.status} | {response.json()}")    # log response before validation

        # Validate response status
        expect(response.status).toBe(status_code)

        # Validate response schema if provided
        if schema:
            try:
                schema.model_validate_json(response.json())
            except ValidationError as e:
                logging.error(f"Schema validation failed: {e}")
                allure.attach(json.dumps(response.json(), indent=2), name="Invalid Response", attachment_type=allure.attachment_type.JSON)
                raise AssertionError("Response schema validation failed!")

        return response