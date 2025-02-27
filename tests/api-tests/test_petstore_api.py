import pytest
import allure
from playwright.sync_api import APIRequestContext
from utils.request_helper import send_request
from api.schema import PetSchema


@allure.title("Get pet details")
def test_get_pet(api_request_context: APIRequestContext):
    response = send_request(api_request_context, "GET", "/pet/1", status_code=200)