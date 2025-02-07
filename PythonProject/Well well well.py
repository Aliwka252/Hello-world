import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.happiness = 50
        self.alive = True

    def to_sleep(self):
        print("Sleeping... zzz")
        self.energy += 5
        self.happiness += 3

    def to_play(self):
        print("Playing with a toy!")
        self.energy -= 3
        self.happiness += 7

    def to_eat(self):
        print("Eating food!")
        self.energy += 10
        self.happiness += 5

    def to_explore(self):
        print("Exploring the surroundings...")
        self.energy -= 4
        self.happiness += 4

    def is_alive(self):
        if self.energy <= 0:
            print("The cat is exhausted and can't continue…")
            self.alive = False
        elif self.happiness <= 0:
            print("The cat is sad and lonely…")
            self.alive = False
        elif self.energy > 100:
            print("The cat is overfed and very happy!")
            self.alive = False

    def end_of_day(self):
        print(f"Energy = {self.energy}")
        print(f"Happiness = {self.happiness}")

    def live(self, day):
        day_label = f"Day {day} of {self.name}'s life"
        print(f"{day_label:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_sleep()
        elif live_cube == 2:
            self.to_play()
        elif live_cube == 3:
            self.to_eat()
        elif live_cube == 4:
            self.to_explore()
        self.end_of_day()
        self.is_alive()

# Main execution
whiskers = Cat(name="Whiskers")
for day in range(365):
    if not whiskers.alive:
        break
    whiskers.live(day)
