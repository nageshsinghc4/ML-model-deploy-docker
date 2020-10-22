# ML-model-deploy-docker

I’m attempting to display an example approach to create some software that can be used by the stakeholders. Specifically, 
we would create a web-service that can be queried to obtain the predictions from a machine learning model. The post is mostly intended for machine learning practitioners who would like to go beyond only developing models.

## Workflow 

1. Training a machine learning model on a local system.
2. Wrapping the inference logic into a flask application.
3. Using docker to containerize the flask application.

Use ```model_train.py``` to train a logistic regression model on the iris dataset and generate a pickled model file (iris_trained_model.pkl)
Use app.py to wrap the inference logic in a flask server to serve the model as a REST webservice:
Execute the command python app.py to run the flask app.
Go to the browser and hit the url 0.0.0.0:5000 to get a message Hello World! displayed. 
Run the below command in terminal to query the flask server to get a reply 2 for the model file provided in this repo:
  
```
curl -X POST \
   0.0.0.0:80/predict \
   -H 'Content-Type: application/json' \
   -d '[5.9,3.0,5.1,1.8]'
```

Run docker ```build -t app-iris .``` to build the docker image using Dockerfile. (Pay attention to the period in the docker build command)
Run docker run -p 80:80 app-iris to run the docker container that got generated using the app-iris docker image. (This assumes that the port in app.py is set to 80)
Use the below command in terminal to query the flask server to get a reply 2 for the model file provided in this repo:
```
curl -X POST \
    0.0.0.0:80/predict \
    -H 'Content-Type: application/json' \
    -d '[5.9,3.0,5.1,1.8]'
```
