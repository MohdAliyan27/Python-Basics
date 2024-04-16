
message = "Hello Python"
print(message)
 
 
message = "Hello World Of Python Programming"
print(message)
 
 
msg = 'good morning "to you"'
print(msg)
 
 
print(msg.title())
 
print(msg.upper())
 
print(msg.lower())
 
 
first_name = 'ernie'
last_name = 'lace'
 
full_name=f"{first_name}  \t   {last_name} \n{msg} {message}"
print(full_name.title())
 
print(full_name.strip())
 
fav_language = '    python   '
 
print(fav_language.strip())
 
url1= 'https://www.google.com'
withoutPrefix = url1.removeprefix('https://')
 
print(withoutPrefix)
 
 
universe_age = 14_000_000_000
#declaring x y z and assigning 0 to them all
x,y,z=0,0,0
 
print(x)
 
 
 
#----------------------------------------------------------------------------------------------------
bicycles = ['trek','cannondale','redline','specialized']
 
print(bicycles[-1].title())
 
print(bicycles[-2].title())
 
 
message = f"My first bicycle was a {bicycles[0].title()}."
#f for making the text formatting
# f stands for formatting string literals, 
#f-strings are string literals that have an f before the opening quotation mark. 
#They can include Python expressions enclosed in curly braces. 
#Python will replace those expressions with their resulting values.
print(message)
 
 
motorcycles = ['honda','yamaha','suzuki']
 
print(motorcycles)
 
motorcycles[0]='ducati'
 
print(motorcycles)
 
motorcycles.append('honda')
print(motorcycles)
 
 
fav_foods =[1,2]
 
fav_foods.append('apple')
 
fav_foods.insert(0,'mango')
 
del fav_foods[0]
 
print(fav_foods)
fav_foods.insert(0,'mango')
 
print(fav_foods)
 
popped_fruit =  fav_foods.pop()
 
print(popped_fruit)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
 
print(f"\n A {too_expensive.title()} is too expensive right now to be in the list")
 
#permanent sorting ,changes the list order permanently in the alphabetical order
motorcycles.sort()
 
print(motorcycles)
 
motorcycles.sort(reverse=True)
 
print(motorcycles)
 
numlist = [45,67,2,4,6,1,100,100]
 
numlist.sort()
 
print(numlist)
 
 
#sorted() method is for temporary sorting
 
cars = ['bmw' , 'audi' ,'toyota','subaru']
 
print(cars)
 
print(sorted(cars,reverse=True))
 
print(cars)
 
length = len(cars)
 
 
 

[10:48 AM] Roopali Bedarkar
SyntaxError: invalid syntax

>>> & C:/Users/bedir/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Roopali/PythonSession/src/print.py

  File "<stdin>", line 1

    & C:/Users/bedir/AppData/Local/Microsoft/WindowsApps/python3.12.exe c:/Roopali/PythonSession/src/print.py

    ^
#Error is "print" is the reserved keyword.
SyntaxError: invalid syntax
[10:48 AM] Muskaan(Trainer) (Unverified)
create  a guest list and practise append insert remove 
also practise pop del
[10:49 AM] Muskaan(Trainer) (Unverified)
share your source codes here in this chat
[10:51 AM] Mohd Aliyan .
guestList= [10,11,5];

print(guestList)

guestList.append(30);

print(guestList)

guestList.insert(1, 100);

print(guestList)

guestList.remove(100)

print(guestList)
