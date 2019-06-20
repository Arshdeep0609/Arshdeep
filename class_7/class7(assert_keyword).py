def KelvintoFahrenheit(Temperature):
    assert(Temperature>=0),"Colder than absolute zero!"
    res=((Temperature-273)*1.8)+32
    return res

try:
    print(KelvintoFahrenheit(273))
    print(KelvintoFahrenheit(505.78))
    print(KelvintoFahrenheit(-5))
except AssertionError as ob:
    print(ob)
print("thank you")
