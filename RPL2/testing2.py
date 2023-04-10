def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function_2(first_name, last_name):
   print(first_name + " " + last_name)

my_function_2(last_name="Tobias", first_name="Emil")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(food):
  for x in food:
    print(x)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def multiply_by_two(a):
  return a * 2

assert(multiply_by_two(3)) == 6

def multiply_by_x(a, x=2):
  "If x not passed, then define the default value to 2"
  return a * x


assert(multiply_by_x(3)) == 6
assert(multiply_by_x(3, 1)) ==3


#user_input = input('input dikali dengan 2: ')
#print(multiply_by_two(int(user_input)))


#how_many_input = input('berpakali ingin nput data')
#i = 0
#while True:
#       user_input = input('input dikali dengan 2: ')
#       print(multiply_by_two(int(user_input)))
#       i ++ 1



