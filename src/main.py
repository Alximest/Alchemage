from datetime import datetime
from pprint import pprint
from pydantic import BaseModel, PositiveInt

class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt] 
    
external_data = {
    'id': 123,
    'name': 'Bolduin',
    'signup_ts': '2019-06-01 12:22',
    'tastes': {
        'wine': 9,
        'potato': 7,
        'cabbage': 1
    },
}

user = User(**external_data)

pprint(user.id)

pprint(user.model_dump)