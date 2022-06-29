def fahrenheitoCelsius(c):
    return 9/5 * c + 32

print ("Grados Fahrenheit     Grados Celsius")
print ("=================     ==============")

for i in range(0,121,10):
    print("        ",i,"°F" "       ",fahrenheitoCelsius(i),"°C")
