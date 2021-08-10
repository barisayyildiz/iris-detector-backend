# Iris Flower Detector - _backend_

### [Frontend](https://github.com/barisayyildiz/iris-detector-frontend)

[Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) from scikit learn is used to predict the iris flower type based on the given flower's **sepal/petal width/height**  
A flower can be either:
* Setosa
* Versicolor
* Virginica

Model is trained with **K-Means Clustering Algorithm** with the cluster number **3**.  
The model is saved inside **iris_model** file  
But you can aslo run all the cells inside **Iris Dataset.ipynb** to train the model and rewrite the model to iris_model file


## Endpoints
### Example Request
`
GET /api/flower
`
```
{
  "sepal_width":2.4,
  "sepal_length":5.6,
  "petal_width":1.3,
  "petal_length":6.7
}
```

### Response
```
{
  "name":"Virginica",
  "url":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/1024px-Iris_virginica_2.jpg"
}
```

To run project:  

```
virtualenv venv  
source venv/bin/activate  
git clone https://github.com/barisayyildiz/iris-detector-backend  
cd iris-detector-backend  
pip install -U -r requirements.txt
python manage.py runserver
```
