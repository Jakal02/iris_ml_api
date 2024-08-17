# iris_ml_api
An ML model that infers Iris species when provided Sepal and Petal measurements with an API service. It uses the famous Iris Dataset.

The purpose of this project is to practice creating and serving a scalable ML app by creating a lightweight async dockerized API service. The containers can be orchestrated in theory with a tool like Kubernetes, and the model is light enough that each instance is designed to store it in memory. 

## Model

The model was built using [CatBoost](https://catboost.ai/). This is a performant and fast boosting algorithm with a rich Python API, making it ideal for this project.

## Backend

The backend is a FASTAPI app.

### Install Just to execute helper script recipes

Just is a handy way to save and run project-specific commands.

Install it to your `$PATH` by following the [instructions here](https://just.systems/man/en/chapter_2.html#installation).

Once installed, from the project root directory, all recipes found in the `justfile` can be run by simply doing

```bash
just <recipe name>
```


### Backend TODO

- [X] create hello world fastapi app with test
- [X] dockerize it
- [X] load model on startup
- [X] create model endpoint that validates args but does nothing
- [X] connect model and endpoint
- [X] Dockerize tests and have them stateful to instantiate model
- [X] write tests for predict route
- [X] speed tests for dockerized app

#### More pie-in-the-sky goals
- [ ] make a database
    - [ ] create a dummy register endpoint
    - [ ] create an empty database to store things
    - [ ] add API key support
