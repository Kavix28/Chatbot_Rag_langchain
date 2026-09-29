"""Environment-backed application settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	"""Runtime configuration loaded from environment variables or .env."""

	qdrant_url: str = "http://localhost:6333"
	qdrant_api_key: str | None = None
	qdrant_collection: str = "enterprise_documents"
	embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
	llm_api_key: str | None = None
	llm_model: str = "gpt-4o-mini"

	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


settings = Settings()
