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

"""
[
  {
    "id": 0,
    "category": {
      "id": 0,
      "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
      "string"
    ],
    "tags": [
      {
        "id": 0,
        "name": "string"
      }
    ],
    "status": "available"
  }
]
"""