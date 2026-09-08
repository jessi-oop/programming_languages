class Dog:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def bark(self):
        return "Woof! woof!"

    def celebrateBirthday(self):
        self._age += 1
        return f"Happy Birthday! {self._name} is now {self._age} years old."

    def get_info(self):
        return {"name": self._name, "age": self._age} 

def main():
    dog = Dog("Paolo", 30)

    print(dog.bark())
    print(dog.celebrateBirthday())
    dog_info = dog.get_info()
    print(f"Dog Name: {dog_info["name"]}, Age: {dog_info["age"]}")

if __name__ == "__main__":
    main()