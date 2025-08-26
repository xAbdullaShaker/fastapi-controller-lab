from pydantic import BaseModel,Field
from typing import Optional

class CommentSchema(BaseModel):
  id: Optional[int] = Field(default=None)
  tea_id: int
  content: str

  class Config:
    orm_mode = True
