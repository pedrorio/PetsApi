import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

templates = Jinja2Templates("pets/templates")
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False, response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
