## print hello world in python
print("Hello World")
print("Hello " + "Perth")

## fstring print
# solve data type problem
friend_name = 'Perth'
friend_age = 29
friend_location = 'Australia'

text = f"{friend_name} is {friend_age} years old and he lives in {friend_location} right now!"

print(text)

## list + control flow
print()
marvels = ['Captain America', 'Iron Man', 'Captain Marvel', 'Dr.Strange']
print("Hello " + marvels[0] + "!!")
print("Hello " + marvels[1] + "!!")
print("Hello " + marvels[2] + "!!")
print("Hello " + marvels[3] + "!!")
## Do not repeat yourself !!!

## for Loop
print()
for hero in marvels:
  print("Hello " + hero + "!!")

print()
for hero in marvels:
  print(f"Hello {hero} awesome!!")