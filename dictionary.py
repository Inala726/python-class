yo = {
    "name": "Jacob Inala",
    "age": "18",
    "gender": "I'd rather not say"
}

car = {
    "brand":"Toyota",
    "model":"Corolla",
    "year":2020,
    "automatic_transmission":True,
    "year":2034,
    "owner":"Prince"
}

# my_dict = {"apple": 1, "banana": 2, "cherry": 1}
# print(my_dict)

# get a single value
# print(car.get("model"))

# get keys
ky = car.keys()
# print(type(ky))
car["tinted"] = True
# print(car)
items = car.items()
# print(type(items))
if "year" in car:
    car["year"] = 2025

for x in car:
    if x.startswith("b"):
        result = x.upper()
        print(result)

mycopy = car.copy()
print(mycopy)

