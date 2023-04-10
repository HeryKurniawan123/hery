
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.door = 'Closed'
        self.car = 'Off'

# Membuka Pintu
    def Open(self):
        if self.door == 'Closed':
            print('Pintu Terbuka')
            self.door = 'Open'
        else:
            print('Pintu Tertutup')

# Menutut pintu
    def Close(self):
        if self.door == 'Open':
            print('Pintu Tertutup')
            self.door = 'Closed'
        else:
            print('Pintu Terbuka')
    
# Menyalakan mesin
    def On(self):
        if self.car == 'Off':
            print('Mesin Nyala')
            self.car = 'On'
        else:
             print('Mesin Mati')

# Mematikan mesin
    def Off(self):
        if self.car == 'On':
            print('Mesin Mati')
            self.car = 'Off'
        else:
            print('Mesin Nyala')



# Memanggil Hasil di atas
car_1 = Car('Honda', 2023)
car_1.Open()
car_1.Close()
car_1.On()
car_1.Off()