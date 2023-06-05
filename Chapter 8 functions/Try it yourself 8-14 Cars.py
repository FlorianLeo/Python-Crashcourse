def make_car(manufacturer, model, **car_params):
	"""Descripe a Car and some details about it"""
	car_params['manufacturer'] = manufacturer
	car_params['model'] = model
	return car_params

car1 = make_car('Subaru', 'Impreza', remote=True, color='blue')
print(car1)