# serializers/tea.py

from pydantic import BaseModel, Field
from typing import Optional, List
from .comment import CommentSchema

class TeaSchema(BaseModel):
  id: Optional[int] = Field(default=None) # This makes sure you don't have to explicitly add an id when sending json data
  name: str
  in_stock: bool
  rating: int
  comments: List[CommentSchema] = []

  class Config:
    orm_mode = True
