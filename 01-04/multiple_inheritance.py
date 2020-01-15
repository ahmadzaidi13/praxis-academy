class Car:
    def __init__(self, name, wheels = 4):
        self.wheels = wheels
class Gasoline(Car):
    def __init__(self, name, engine = 'Gasoline', tank_cap=20):
        Car.__init__(self, name)
        self.name = name
        self.engine = engine
        self.tank_cap = tank_cap
        self.tank = 0
    def refuel(self):
        self.tank = self.tank_cap
class Electric(Car):
    def __init__(self, name, engine='Electric', kWh_cap=60):
        Car.__init__(self, name)
        self.name = name
        self.engine = engine
        self.kWh_cap = kWh_cap
        self.kWh = 0
    def recharge(self):
        self.kWh = self.kWh_cap
class Hybrid(Gasoline, Electric):
    def __init__(self, name, engine='Hybrid', tank_cap=1, kWh_cap=5):
        Gasoline.__init__(self, name, engine, tank_cap)
        Electric.__init__(self, name, engine, kWh_cap)

yaris = Gasoline('Toyota Yaris')
model3 = Electric('Tesla Model 3')
prius = Hybrid('Toyota Prius')

print (yaris.name)
print (yaris.__dict__)
print ("")
print (model3.name)
print (model3.__dict__)
print ("")
print (prius.name)
print (prius.__dict__)