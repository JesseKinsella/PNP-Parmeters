def hi_nick():
  print("Hello, Nick!")

hi_nick()

#parmeters are a way to pass information into a function

def hi_person(name):
  print(f"Hello, {name}!")

hi_person("Jesse") #pass anything into function

def add_numbers(num1, num2):
  print(num1+num2)

add_numbers(34,1)
add_numbers(100,-1)

#created a function called dog_info that takes in a dog's age and name and prints a sentence about the dog

def dog_info(age,dname):
  print(f"{dname} is a great dog and is {age} year(s) old")

dog_info(1,'Oliver')
  