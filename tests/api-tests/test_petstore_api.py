import pytest
import allure
from playwright.sync_api import APIRequestContext
from api.schema import CommonResponseSchema, InvalidPetSchema, PetSchema, IdNameSchema
from api.petstore_api import PetStoreApi, send_request
import os

@pytest.fixture(scope='function')
def pet_store_api(api_request_context: APIRequestContext):
    return PetStoreApi(api_request_context)


@allure.title("Get pet details")
def test_get_pet(pet_store_api):
    pet_id = 1
    pet = pet_store_api.get_pet(pet_id)
    assert pet.id == pet_id
    assert pet.name == 'Rex'
    assert pet.photoUrls == ["http://example.com/photo.jpg"]
    assert pet.status == 'available'
    assert pet.category.id == 1
    assert pet.category.name == 'dog'

@allure.title("Add a new pet")
def test_add_pet(pet_store_api):
    pet = PetSchema(
        id=1,
        category=IdNameSchema(id=1, name='Dogs'),
        name='doggie',
        photoUrls=['string'],
        tags=[],
        status='available'
    )
    new_pet = pet_store_api.add_pet(pet)
    assert new_pet.id == pet.id
    assert new_pet.name == pet.name
    assert new_pet.photoUrls == pet.photoUrls
    assert new_pet.status == pet.status
    assert new_pet.category.id == pet.category.id

@allure.title("Update pet details")
def test_update_pet(pet_store_api):
    pet_store_api.update_pet(pet_id=1, name='Rex', status='sold')

@allure.title("Delete pet")
def test_delete_pet(pet_store_api):
    pet_id = 1
    pet_store_api.delete_pet(pet_id)

@allure.title("Get pet by status")
@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_get_pet_by_status(pet_store_api, status):
    pets = pet_store_api.get_pet_by_status(status)
    for pet in pets:
        assert pet['status'] == status

@allure.title("Get pet with invalid ID")
@pytest.mark.parametrize('id', [1e15, '1a0', -12])
def test_get_pet_invalid_id(pet_store_api,id):
    send_request(
        pet_store_api.api_context,
        method='GET',
        endpoint=f'{pet_store_api.path}/{id}',
        status_code=404,
        schema=CommonResponseSchema
    )

@allure.title("Add pet with invalid id field")
def test_add_pet_missing_fields(pet_store_api):
    invalid_pet = InvalidPetSchema(
        id='1a',
        category=IdNameSchema(id=1, name='Dogs'),
        name='doggie',
        photoUrls=['string'],
        tags=[],
        status='available'
    )
    response = send_request(
        pet_store_api.api_context,
        method='POST',
        endpoint=f'{pet_store_api.path}',
        status_code=500,
        extra_headers={'Content-Type': 'application/json'},
        data=invalid_pet.model_dump(),
        schema=CommonResponseSchema
    )
    assert response.message == 'something bad happened'
    assert response.code == 500
    assert response.type == 'unknown'
