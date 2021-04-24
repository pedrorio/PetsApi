import fastapi

from pets import schemas, services

router = fastapi.APIRouter()


@router.get('/api/weather', response_model=schemas.Weather)
async def get_the_weather_report(location: schemas.Location = fastapi.Depends()):
    return await services.weather.get_weather(location)