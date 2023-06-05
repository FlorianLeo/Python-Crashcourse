from ElectricCarClasses import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.getDescriptiveName())
my_tesla.energyStorage.describeBattery()
my_tesla.energyStorage.getMilageEstimate()