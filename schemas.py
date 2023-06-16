from pydantic import BaseModel


class Analyze(BaseModel):
    id: int
    text: str
    sentiment: str
    
    class Config:
        orm_mode = True
    

class AnalyzeCreate(BaseModel):
    text: str
    
    
    