from datetime import datetime

import pytz
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app_python")


def get_time(request: Request, timezone: str = "Europe/Moscow") -> str:

    return templates.TemplateResponse(
        "time_template.html",
        {"request": request, "current_time": get_tz_time(timezone)},
    )


def get_tz_time(timezone) -> str:

    return datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")
