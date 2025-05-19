
from google.adk.agents import Agent

# Tools
from tools.weather import get_weather
from tools.time import get_current_time



root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agente para responder a preguntas sobre la hora y el tiempo en una ciudad."
    ),
    instruction=(
        "Eres un agente servicial que puede responder a las preguntas de los usuarios sobre la hora y el tiempo en una ciudad."
    ),
    tools=[get_weather, get_current_time],
)