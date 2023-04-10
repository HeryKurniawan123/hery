#UNPACKING USING ASTERISK

fruits = ("apple", "banana", "cherry", "strawberry", "rasberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#contoh <<<

cars = {
    'brand': 'honda',
    'product': 'civic'
}
print(cars['brand'])

print(cars.keys())

for key in cars.keys():
    print(cars[key])

cars = {
    'brand' : 'honda',
    'product': 'civic'
}


assert(list(cars.keys())[1]) == 'product'

print(cars.values())

print(cars.get('year', 'none'))
print('Tidak akan dijalankan')

if 'year' in cars:
    print (cars['year']) #cars.get('year','none')

cars.update(
    {
        'year': 2020,
        'key2' : 2021
    }
)
cars['year'] = 2020
print(cars)

cars['brand'] = 'Toyota'
print(cars)

