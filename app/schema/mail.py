#!/usr/bin/env python3
from pydantic import BaseModel


class Mail(BaseModel):
    name: str
    email: str
    discovery_source: str
    message: str

    class Config:
        from_attributes = True
