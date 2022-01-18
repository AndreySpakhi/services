from pyowm import OWM

owm = OWM('114e5930a52a6f6ea90ad0c2d3054a42')
mgr = owm.weather_manager()

place = input("В каком городе/стране?")

observation = mgr.weather_at_place(place)
w = observation.weather

print(w.temperature('celsius')["temp"])