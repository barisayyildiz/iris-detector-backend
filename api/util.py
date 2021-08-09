import pickle
import os

def predict(obj):
	sepal_width = obj["sepal_width"]
	sepal_length = obj["sepal_length"]
	petal_width = obj["petal_width"]
	petal_length = obj["petal_length"]

	target_names = ['Setosa', 'Versicolor', 'Virginica']

	print(os.listdir())

	filename = 'iris_model'
	infile = open(filename, 'rb')
	model = pickle.load(infile)

	infile.close()

	return target_names[int(model.predict([[sepal_width, sepal_length, petal_width, petal_length]]))]

