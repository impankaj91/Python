class Animals:
    type="Pet"

class Pet(Animals):
    name="Dog"

class Sound(Pet):
    sound="Bow Bow"

s=Sound()
print(f"Type of Animal is {s.type}\n Name is {s.name} and sound is {s.sound}\n***************")
