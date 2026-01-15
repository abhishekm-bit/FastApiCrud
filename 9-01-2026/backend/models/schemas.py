from pydantic import BaseModel

class SyllabusRequest(BaseModel):
    url:str
    course:str
    level:str
    duration:str
