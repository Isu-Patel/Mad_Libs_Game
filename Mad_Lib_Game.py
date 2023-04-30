# Mad Libs Project
print("Welcome to the Mad Lib Game.🎉")
print("")

noun = str(input("Enter a Noun: "))
verb = str(input("Enter a Verb: "))
adjective = str(input("Enter a Adjective: "))
animal = str(input("Enter a Animal: "))
place = str(input("Enter a Place: "))
color = str(input("Enter a Color: "))


story = f"The {adjective} {animal} {verb} over the {color} {noun} in {place}."

print("")
print("Here is your Mad Libs Story: ")
print(story)
