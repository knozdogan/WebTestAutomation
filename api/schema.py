from pydantic import BaseModel
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
    category: Optional[IdNameSchema]
    photoUrls: Optional[list]
    tags: Optional[IdNameSchema]