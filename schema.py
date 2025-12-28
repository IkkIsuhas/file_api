from pydantic import BaseModel

class chatRequest(BaseModel):
    prompt : str

class chatResponse(BaseModel):
    id : int
    prompt : str
    note : str