'''class PA:
    total_animals = 0

    def __init__(self, name, sp, fly, swim, run):
        # Атрибути рівня об'єкту
        self.name = name
        self.sp = sp
        self.fly = fly
        self.swim = swim
        self.run = run

        PA.total_animals += 1

    def make_sound(self):
        if self.sp == "Тигр":
            return "Рррр"
        elif self.sp == "Птах":
            return "Чирик"
        elif self.sp == "Риба":
            return "Буль"
        elif self.sp == "Крокодил":
            return "Гррр"

    def action(self):
        if self.fly:
            return f"{self.name} летить."
        elif self.swim:
            return f"{self.name} плаває."
        elif self.run:
            return f"{self.name} біжить."
        else:
            return f"{self.name} не вміє нічого."

tiger = PA("Тигр", "Тигр", False, False, True)
parrot = PA("Папуга", "Птах", True, False, False)
fish = PA("Золота рибка", "Риба", False, True, False)
crocodile = PA("Крокодил", "Крокодил", False, True, True)

print(tiger.make_sound())
print(parrot.action())
print(fish.make_sound())
print(crocodile.action())

print(f"Загальна кількістьтварин: {PA.total_animals}")'''


class Car:
    fuel_type = "Бенз"

    def __init__(self, make, model, year, color, speed, is_running=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
        self.is_running = is_running


    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.make} {self.model} заведена."
        else:
            return f"{self.make} {self.model} працює."

    def stop(self):
        if self.is_running:
            self.is_running = False
            return f"{self.make} {self.model} зупинена."
        else:
            return f"{self.make} {self.model} вже зупинена."

    def accelerate(self, new_speed):
        if self.is_running:
            self.speed = new_speed
            return f"{self.make} {self.model} розганяється до {new_speed} км/год."
        else:
            return f"{self.make} {self.model} не може розганятися, оскільки не працює."

    def brake(self):
        if self.is_running:
            self.speed = 0
            return f"{self.make} {self.model} зупиняється."
        else:
            return f"{self.make} {self.model} не може зупинятися."


car1 = Car("Kopeyika", "Vaz-2101", 2022, "Сірий", 0)
car2 = Car("Mitsubishi", "Outlander", 2021, "Червоний", 0)

print(car1.start())

print(car1.accelerate(50))

print(car1.brake())

print(car2.stop())

print(car2.color)

print(car2.year)

print(f"Тип пального: {Car.fuel_type}")