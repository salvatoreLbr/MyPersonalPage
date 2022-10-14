from pathlib import Path
from os import path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn


# Initialize FastAPI app
app = FastAPI()

# Get relative path
path_str = Path(path.dirname(path.realpath(__file__)))

# Mount static file as css
app.mount("/static", StaticFiles(directory=path_str.joinpath("static")), name="static")

# Set templates html path
templates = Jinja2Templates(directory=path_str.joinpath("templates"))


#####################
##### GET route #####
#####################

# Login route
@app.get("/", response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request}
    )

if __name__ == "__main__":
    uvicorn.run(
        "src.mypersonalpage.app:app", host="127.0.0.1", port=5000, log_level="info"
    )