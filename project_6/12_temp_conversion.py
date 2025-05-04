# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) 
# that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Static method to convert Celsius to Fahrenheit
temp_c = 32  # Celsius temperature
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c) # Calling the static method
print(f"{temp_c}°C is equal to {temp_f}°F")  # Output the result