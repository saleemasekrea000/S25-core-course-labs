from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Request

from app_python.app_service import get_time

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def show_time(request: Request):
    return get_time(request)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
