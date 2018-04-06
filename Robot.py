class Robot:
    noOfRobots = 0 #class variable
    def __init__(self,name=None,build_year=None):
        self.name=name
        self.build_year=build_year
        Robot.noOfRobots += 1

    @classmethod
    def print_noOfRobots(cls):
        print("No of Robots existed in the world is",cls.noOfRobots)

    def say_hi(self):
        if self.name:
            print("Hi, I am "+ self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," +  str(self.build_year) +  ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " +  str(self.build_year)

    def __del__(self):
        print(self.name,"is destroying.... Bye.")
        Robot.noOfRobots -= 1


if __name__ == "__main__":
    x = Robot("Henry", 2008)
    y = Robot()
    y.set_name("Marvin")
    y.set_build_year(2010)
    x.say_hi()
    print(str(y))
    print(repr(y))
    Robot.print_noOfRobots()
    del y
    Robot.print_noOfRobots()
