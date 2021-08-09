import pickle
import os

def predict(obj):
	sepal_width = obj["sepal_width"]
	sepal_length = obj["sepal_length"]
	petal_width = obj["petal_width"]
	petal_length = obj["petal_length"]

	target_names = ['Setosa', 'Versicolor', 'Virginica']
	urls = [
		"https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/330px-Kosaciec_szczecinkowaty_Iris_setosa.jpg",
		"https://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg",
		"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1024px-Iris_virginica_2.jpg"
	]

	filename = 'iris_model'
	infile = open(filename, 'rb')
	model = pickle.load(infile)

	infile.close()

	print(f'num : {model.predict([[sepal_length, sepal_width, petal_length, petal_width]])}')

	index = int(model.predict([[sepal_length, sepal_width, petal_length, petal_width]]))
	name = target_names[index]

	return {
		"name":name,
		"url":urls[index]
	}

