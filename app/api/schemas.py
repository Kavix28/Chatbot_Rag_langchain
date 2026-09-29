"""Pydantic request and response schemas."""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Input for a grounded chat query."""

    question: str


class ChatResponse(BaseModel):
    """Grounded answer returned by the chat API."""

    answer: str