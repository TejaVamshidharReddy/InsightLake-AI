from fastapi import FastAPI

app = FastAPI(
    title="InsightLake AI API",
    version="0.1.0",
    description="API layer for curated analytics and AI-assisted insights.",
)

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to InsightLake AI"}
