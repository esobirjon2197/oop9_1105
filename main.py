

# 9-m
class Robot:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def work(self, hours):
        print(f"{self.name} {hours} soat ishladi")


class Lamp:
    def turn_on(self):
        print("Chiroq yoqildi")


class Factory:
    def run_robot(self, robot, hours):
        if hasattr(robot, "work"):
            robot.work(hours)
        else:
            print("work method topilmadi")


robot = Robot("Robo1", 100)
lamp = Lamp()

factory = Factory()
factory.run_robot(robot, 5)

factory.run_robot(lamp, 5)
