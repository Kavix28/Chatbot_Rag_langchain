"""HTTP API routes."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict[str, str]:
    """Report that the API process is running."""
    return {"status": "ok"}