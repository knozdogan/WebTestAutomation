from locust import HttpUser, task, between

class SearchLoadTest(HttpUser):
    wait_time = between(1, 3)  # Simulates a real user's delay between actions

    @task
    def search_product(self):
        query = "Laptop"  # Example search term
        response = self.client.get(f"/arama?q={query}")
        assert response.status_code == 200, f"Search failed with status {response.status_code}"