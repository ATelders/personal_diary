from datetime import datetime
from io import StringIO
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    name = 'Doe'
    first_name = 'John'
    email = 'jd@gmail.com'

class Diary_entry(BaseModel):
    user_id : int
    date : str
    content : str
    emotion : str