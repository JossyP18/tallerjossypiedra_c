def F_to_K(temperature):
    """Convierte temperaturas de Fahrenheit a Kelvin."""
    return (5/9) * (temperature - 32) + 273.15

def C_to_R(temperature):
    """Convierte temperaturas de Celsius a Rankine."""
    return (temperature + 273.15) * 9/5

def C_to_F(temperature):
    """Convierte temperaturas de Celsius a Fahrenheit."""
    return temperature * 1.8 + 32