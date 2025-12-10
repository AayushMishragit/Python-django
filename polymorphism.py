class Bird:
    def sound(self):
        print("chirp")


class Cat:
    def sound(self):
        print("Meaw")

animals = [Bird(),Cat()]
for animal in animals:
    animal.sound()        #https://api.github.com/