from schema import PetSchema
from playwright.sync_api import APIRequestContext
from utils.request_helper import send_request
from utils.step_decorator import step

class PetStoreApi:
    def __init__(self, api_context: APIRequestContext):
        self.api_context = api_context
        self.path = '/pet'

    @step('Get pet')
    def get_pet(self, pet_id: int) -> PetSchema:
        response = send_request(
            self.api_context,
            method='GET',
            endpoint=f'{self.path}/pet/{pet_id}',
            status_code=200,
            schema=PetSchema
        )
        response_json = response.json()
        return PetSchema(**response_json)
    
    @step('Add pet')
    def add_pet(self, pet: PetSchema) -> PetSchema:
        response = send_request(
            self.api_context,
            method='POST',
            endpoint=f'{self.path}/pet',
            status_code=200,
            data=pet.model_dump(),
            schema=PetSchema
        )
        response_json = response.json()
        return PetSchema(**response_json)
    
    @step('Update pet')
    def update_pet(self, pet: PetSchema) -> PetSchema:
        response = send_request(
            self.api_context,
            method='PUT',
            endpoint=f'{self.path}/pet',
            status_code=200,
            data=pet.model_dump(),
            schema=PetSchema
        )
        response_json = response.json()
        return PetSchema(**response_json)
    
    @step('Delete pet')
    def delete_pet(self, pet_id: int):
        send_request(
            self.api_context,
            method='DELETE',
            endpoint=f'{self.path}/pet/{pet_id}',
            status_code=200
        )
    
    