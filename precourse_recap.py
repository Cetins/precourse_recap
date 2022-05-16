fahrenheit_temperature = int(input("Enter temperature in Fahrenheit: "))

def convert_temperature(temperature):
    temperature = round((fahrenheit_temperature - 32) * 5/9)
    print("Temperature in Celcius:", temperature)

convert_temperature(fahrenheit_temperature)