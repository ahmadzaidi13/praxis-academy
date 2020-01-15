class vehicle:
    def __init__(self, name, wheels, capacity):
        self. name = name
        self. wheels = wheels
        self.capacity = capacity

class car(vehicle):
    def __init__(self, name):
        self.name = name
        self.wheels = 4
        self.capacity = 5

class motorcycle(vehicle):
    def __init__(self, name):
        self.name = name
        self.wheels = 2
        self.capacity = 2
                
subaru = car('Subaru')
supra = motorcycle('Supra')

print (subaru.name)
print("jumlah roda:", subaru.wheels)
print("kapasitas:", subaru.capacity)

print (" ")

print (supra.name)
print("jumlah roda:", supra.wheels)
print("kapasitas:", supra.capacity)


