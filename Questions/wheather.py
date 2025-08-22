# Write a program that will determine whether the value of temperature and humidity is provided by the user.

# | TEMPERATURE(C) | HUMIDITY(%) |     WEATHER    |
# |----------------|-------------|----------------|
# |      >= 30     |    >= 90    | Hot and Humid  |
# |      >= 30     |    <  90    |      Hot       |
# |      <  30     |    >= 90    | Cold and Humid |
# |      <  30     |    <  90    |      Cold      |


temp = float(input("Enter Temprature in °C : "))
humidity = float(input("Enter Humidity : "))

if temp >= 30 and humidity >=90:
  print("Hot and Humid")
elif temp < 30 and humidity >= 90:
  print("Cold and Humid")
else:
  print("Cold")

