from locust import HttpUser, task, between

class GudlftUser(HttpUser):
    wait_time = between(1, 5)

    email_test = "john@simplylift.co"
    club_name = "Simply Lift"
    competition_name = "Spring Festival"

    def on_start(self):
        self.client.get("/", name="Index")
        self.client.post("/showSummary", data={'email': self.email_test}, name="Login")

    @task
    def test_dashboard(self):
        self.client.get("/dashboard", name="Dashboard")

    @task
    def test_booking_page(self):
        self.client.get(
            f"/book/{self.competition_name}/{self.club_name}",
            name="Page Reservation"
        )

    @task
    def test_purchase(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,
                "club": self.club_name,
                "competition": self.competition_name
            },
            name="Achat Place"
        )