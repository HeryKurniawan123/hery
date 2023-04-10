# menunjukkan waktu sekarang
import datetime

x = datetime.datetime.now()
print((x))

# melihat type data datatime
import datetime

x = datetime.datetime.now()
print(type(x))

# menunjukkan tahun dan hari
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# menunjukkan jam, menit, second, microsecond, dan tzone sesuai wilayah
import datetime

x = datetime.datetime(2023, 4, 3)

print(x)

# menunjukkan tanggal, bulan, tahun
import datetime

x = datetime.datetime.now()

print(x.strftime("%d/%m/%Y"))

# menentukan bilangan terkecil dan terbesar dari array
arr_1 = [5, 78, 2, 0]

assert(min(arr_1)) == 0

assert(max(arr_1)) == 78

# function 5 pangkat 5
assert(pow(5, 5)) == 3125


try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try excpt' is finished")



import json

# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary:
print(y["age"])


import json

# a python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

#convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

f = open("demofile.txt")

f = open("demofile.txt", "rt")


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the file does not exist")