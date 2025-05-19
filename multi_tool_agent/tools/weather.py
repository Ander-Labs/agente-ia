

def get_weather(city: str) -> dict:
    """Recupera el informe meteorológico actual de una ciudad especificada.

    Args:
        city (str): El nombre de la ciudad de la que se desea obtener el parte meteorológico.

    Devuelve:
        dict: estado y msg de resultado o error.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


