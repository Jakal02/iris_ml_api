import random
from locust import HttpUser, task, between


class ModelUser(HttpUser):
    wait_time = between(0.5,3)

    # @task
    # def ping_index(self):
    #     self.client.get("/")

    @task
    def query_model(self):
        data = {
                "sepal_length": random.uniform(3,9),
                "sepal_width": random.uniform(1.8, 5.5),
                "petal_length": random.uniform(0.8,7),
                "petal_width": random.uniform(0.1,3)
            }

        self.client.post("/model/predict", json=data)
