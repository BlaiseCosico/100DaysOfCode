cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
   #'Grand Cherokee, Cherokee, Trailhawk, Trackhawk'
    return ', '.join(jeep for jeep in cars['Jeep'])

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    # ['Falcon', 'Commodore', 'Maxima', 'Civic', 'Grand Cherokee']
    return [jeep[0] for jeep in cars.values()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    #['Trailblazer', 'Trailhawk']
    models = []
    for car in cars.values():
    	for c in car:
    		if grep.lower() in c.lower():
    			models.append(c)
    models.sort()
    return models



def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for val in cars.values():
    	val.sort()

    return cars



def main():
	print(get_all_jeeps())
	print(get_first_model_each_manufacturer())
	print(get_all_matching_models())
	print(sort_car_models())

if __name__ == '__main__':
	main()