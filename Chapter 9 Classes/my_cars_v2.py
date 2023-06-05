from carClasses import Car
from ElectricCarClasses import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.getDescriptiveName())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.getDescriptiveName())