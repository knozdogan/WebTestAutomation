from api.schema import PetSchema, ListPetSchema, CommonResponseSchema
from playwright.sync_api import APIRequestContext
from utils.request_helper import send_request
import allure
import os
from dotenv import load_dotenv

if not os.getenv('API_KEY'):
    load_dotenv()

class PetStoreApi:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context
        self.path = 'pet'

    @allure.step('Get pet')
    def get_pet(self, pet_id: int) -> PetSchema:
        response = send_request(
            self.api_context,
            method='GET',
            endpoint=f'{self.path}/{pet_id}',
            status_code=200,
            schema=PetSchema
        )
        return response
    
    @allure.step('Add pet')
    def add_pet(self, pet: PetSchema) -> PetSchema:
        response = send_request(
            self.api_context,
            method='POST',
            endpoint=f'{self.path}',
            status_code=200,
            extra_headers={'Content-Type': 'application/json'},
            data=pet.model_dump(),
            schema=PetSchema
        )
        return response
    
    @allure.step('Update pet')
    def update_pet(self, pet_id: int, name: str = None, status: str = None) -> PetSchema:
        response = send_request(
            self.api_context,
            method='POST',
            endpoint=f'{self.path}/{pet_id}',
            status_code=200,
            extra_headers={'Content-Type': 'application/x-www-form-urlencoded'},
            form_data={'name': name, 'status': status},
            schema=CommonResponseSchema
        )
        return response
    
    @allure.step('Delete pet')
    def delete_pet(self, pet_id: int):
        send_request(
            self.api_context,
            method='DELETE',
            endpoint=f'{self.path}/{pet_id}',
            status_code=200,
            extra_headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'api_key': os.getenv('API_KEY')
                },
            schema=CommonResponseSchema
        )

    @allure.step('Get pet by status')
    def get_pet_by_status(self, status: str) -> list[PetSchema]:
        response = send_request(
            self.api_context,
            method='GET',
            endpoint=f'{self.path}/findByStatus?status={status}',
            status_code=200,
            schema=ListPetSchema
        )
        return response.root
    
