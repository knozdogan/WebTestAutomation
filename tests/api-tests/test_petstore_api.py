import pytest
import allure
from playwright.sync_api import APIRequestContext
from api.schema import PetSchema, IdNameSchema
from api.petstore_api import PetStoreApi

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
