fahrenheit_temperature = int(input("Enter temperature in Fahrenheit: "))

#print(fahrenheit_temperature)

def convert_temperature(temperature):
    temperature = round((fahrenheit_temperature - 32) * 5/9)
    print("Temperature in Celcious:", temperature)

convert_temperature(fahrenheit_temperature)