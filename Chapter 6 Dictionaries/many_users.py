users = {
	'aeisntein':{
		'surname':'albert',
		'lastname':'einstein',
		'location':'princeton'
	},
	'mcurie':{
		'surname':'marie',
		'lastname':'curie',
		'location':'paris'
	}
}

for key, value in users.items():
	print(f'\nBenutzername: {key}')
	full_name = f"{value['surname']} {value['lastname']}"
	location = value['location']
	print(f'\tFull name: {full_name.title()}')
	print(f'\tPlace of Living: {location.title()}')