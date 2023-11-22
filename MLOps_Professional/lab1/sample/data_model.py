from pydantic import BaseModel

class MaintenancePayload(BaseModel):
    temperature: int

class SupportBotPayload(BaseModel):
    query: str