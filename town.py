town = {"city":"Москва", "temperature":20}
print(town)

town['temperature'] = town['temperature'] - 5
print(town)

print(town.get('country','Россия'))

town['date'] = '27.05.2017'
print(town)

print(len(town))
