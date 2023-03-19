from pydantic import BaseModel



class Metadata(BaseModel):
    start_state: str
    end_state: list[str]


class RelationContent(BaseModel):
    write: str
    next_state: str
    move: str

class Config(BaseModel):
    config: dict[str, dict[str, RelationContent]]


class Combine(BaseModel):
    metadata: Metadata
    config: Config
