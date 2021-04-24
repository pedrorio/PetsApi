import httpx

from pets import schemas


async def get_weather(location: schemas.Location):
    url = f'https://weather.talkpython.fm/api/weather/?city={location.city}&country={location.country}'

    if location.state:
        url += f'&state={location.state}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

        data = response.json()

    weather = data.get('weather', {})
    category = weather.get('category', 'UNKNOWN')

    forecast = data.get('forecast', {})
    temperature = forecast.get('temp', 0.0)

    bring_umbrella = category.lower().strip() in {'rain', 'mist'}

    return schemas.Weather(bring_umbrella=bring_umbrella, temperature=temperature, category=category)
