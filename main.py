from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/hello_query")
def hello_query(name: str = "User", place: str = "my website"):
    message = f"Hello {name}! Welcome to {place}"
    return {"message": message}


@app.get("/", response_class=HTMLResponse)
async def serve_html(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
