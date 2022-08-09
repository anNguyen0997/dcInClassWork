# Create a Cat/Dog game, create a class for both the cat and dog. Both animals should have the following properties:
#breed, weight, fur color, name
# Each animal will make their own unique sound
# Cat/Dog class which can do everything that both animals can do, but in its unique twist

class Cat:
    def __init__(self, breed: str, weight: int, furColor: str, name: str):
        self.breed = breed 
        self.weight = weight
        self.furColor = furColor
        self.name = name
    def scratch(self):
        print('scratched.')


class Dog:
    def __init__(self, breed: str, weight: int, furColor: str, name: str):
        self.breed = breed
        self.furColor = furColor
        self.weight = weight
        self.name = name
    def bark(self):
        print('barked!')
        

class Cat_Dog(Cat, Dog):
    def catdogQuirk(self):
        print('Meowoof')



catDog = Cat_Dog('persian husky', 60, 'black', 'kyoto')
catDog.bark()
catDog.scratch()
catDog.catdogQuirk()

cat = Cat('persian', 50, 'white', 'cat')
cat.scratch()

dog = Dog('pitbull', 60, 'grey', 'pitbull')
dog.bark()