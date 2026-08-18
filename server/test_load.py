import util as u

u.load_saved_artifacts()
print('locations count =', len(u.get_location_names()))
print('first5 =', u.get_location_names()[:5])
print('sample =', u.get_estimated_price('1st phase jp nagar', 1000, 2, 2))
