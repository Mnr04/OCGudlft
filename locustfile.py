from locust import HttpUser, task, between

class GudlftUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_welcome(self):
        self.client.get("/")

    @task
    def test_dashboard(self):
        self.client.get("/dashboard")

    @task
    def test_login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})