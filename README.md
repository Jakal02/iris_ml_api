# iris_ml_api
An ML model that infers Iris species when provided Sepal and Petal measurements with an API service. It uses the famous Iris Dataset.

The purpose of this project is to practice creating and serving a scalable ML app by creating a lightweight async dockerized API service. The containers can be orchestrated in theory with a tool like Kubernetes, and the model is light enough that each instance is designed to store it in memory. 

## Model

The model was built using [CatBoost](https://catboost.ai/). This is a performant and fast boosting algorithm with a rich Python API, making it ideal for this project.

## Backend

The backend is a FASTAPI app.


### Backend TODO

- [X] create hello world fastapi app with test
- [ ] dockerize it
- [ ] load model on startup
- [ ] create model endpoint that validates args but does nothing
- [ ] connect model and endpoint
- [ ] speed tests for dockerized app

#### More pie-in-the-sky goals
- [ ] make database stateful
    - [ ] create a dummy register endpoint
    - [ ] create an empty database to store
    - [ ] add API key support
