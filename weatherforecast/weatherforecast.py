from pyowm import OWM

owm = OWM('your token here')
mgr = owm.weather_manager()

place = input("В каком городе/стране?")

observation = mgr.weather_at_place(place)
w = observation.weather

print(w.temperature('celsius')["temp"])