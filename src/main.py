import uvicorn

if __name__ == "__main__":
    uvicorn.run("api.routes:app", port=8080, reload=True)