class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return ((celsius * (9/5)) + 32)
    
    @staticmethod
    def fahrenheit_to_celcius(fahrenheit):
        return ((fahrenheit - 32)* (5/9))
    
    @classmethod
    def info(cls):
        print(f"This is a class method in {cls.__name__}")

print(TemperatureConverter.celsius_to_fahrenheit(45))
print(TemperatureConverter.fahrenheit_to_celcius(23))
TemperatureConverter.info()


