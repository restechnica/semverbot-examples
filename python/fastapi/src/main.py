import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

try:
    from settings.version import VERSION
except:
    VERSION = "0.0.0-LOCAL"

app = FastAPI()


@app.get("/")
async def hello_world():
    return "Hello world"


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="SBOT example",
        version=VERSION,
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")