from fastapi import FastAPI

app = FastAPI(
    title="FastAPI App",
    description="A simple FastAPI application",
    version="1.0.0"
)


@app.get("/")
async def root():
    """Root endpoint returning a welcome message."""
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
