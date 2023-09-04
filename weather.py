import python_weather

import asyncio
import os

async def getweather():
  # Обьявить клиент, поставить значиения по умолчанию(Цельсий, Фаренгейт, кг, метр и тд)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # Получение данных о погоде с города
    weather = await client.get('Astana')
    
    # Вывод температуры в int
    print(f"It's {weather.current.temperature} degrees celsius outside, {weather.current.description}!")
    
    # # Получение погода на последующие несколько дней
    # for forecast in weather.forecasts:
    #   print(forecast)
      
    #   # Часовые данные о погоде
    #   for hourly in forecast.hourly:
    #     print(f' --> {hourly!r}')

if __name__ == '__main__':
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather())