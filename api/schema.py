from pydantic import BaseModel, RootModel
from typing import Optional

class IdNameSchema(BaseModel):
    """
    Pydantic schema for IdName object.
    """
    id: int
    name: str


class PetSchema(BaseModel):
    """
    Pydantic schema for Pet object.
    """
    id: int
    name: str
    status: Optional[str]
    category: IdNameSchema
    photoUrls: Optional[list]
    tags: Optional[list[IdNameSchema]]

ListPetSchema = RootModel(list[PetSchema])

class CommonResponseSchema(BaseModel):
    """
    Pydantic schema for common response object.
    """
    code: int
    type: str
    message: str

class InvalidPetSchema(BaseModel):
    """
    Pydantic schema for Pet object.
    """
    id: str
    name: str
    status: Optional[str]
    category: IdNameSchema
    photoUrls: Optional[list]
    tags: Optional[list[IdNameSchema]]