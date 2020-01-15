class vehicle:
    def __init__(self, name, average_speed):
        self.name = name
        self.average_speed = average_speed

class land_vehicle(vehicle):
    def __init__(self, name,average_speed,wheels):
        super().__init__(name,average_speed)
        self.wheels = wheels

yaris = land_vehicle('yaris',60, 4)

print (yaris.__dict__)
