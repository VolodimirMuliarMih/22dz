# staticmethod
class Person():
    adult_1s = int()
    male = int()
    female = int()
    third_gender = int()

    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        if age > 18:
            Person.adult_1s += 1
        if gender == 'F':
            Person.female += 1
        elif gender == "M":
            Person.male += 1
        else:
            Person.third_gender += 1

    @staticmethod
    def school():
        print('Щкола № 256')

    @classmethod
    def adult(cls):
        print("количество совершеннолетних", cls.adult_1)

    @classmethod
    def gender_is(cls):
        print('количество девочек в классе:', cls.female)
        print('количество мальчиков в классе:', cls.male)
        print(f'и тех кто не определился:', cls.third_gender)

per_1 = Person('Inna', "Petrovs", 25, 'F')
per_2 = Person('Sergey', "Ivanov", 28, 'M')
per_3 = Person("Tanya", "Petrova", 12, "F")
per_4 = Person("Ivan", "Pupkin", 44, 'ThirdGender')
per_1.school()

print(Person.adult_1s)
print(Person.female)
print(Person.gender_is())
