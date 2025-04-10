"""Document-Text-Extraction - API main app."""

from fastapi import FastAPI  # type: ignore

from app.api.v1.routers import document_text_extraction as v1_document_text_extraction
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

# Registrar routers para cada versión
app.include_router(
    v1_document_text_extraction.router, 
    prefix="/v1/document_text_extraction", 
    tags=["Document-Text-Extraction v1"],
)


@app.get("/")
def read_root() -> dict:
    """Read root."""
    return {"message": "API with versioning is running"}
