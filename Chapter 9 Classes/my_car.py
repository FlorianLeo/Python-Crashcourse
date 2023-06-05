from carClasses import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.getDescriptiveName())

my_new_car.odometer_reading = 23
my_new_car.readOdometer()