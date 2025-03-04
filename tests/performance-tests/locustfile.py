from locust import HttpUser, task, between

class SearchLoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def search_product(self):
        query = "Laptop" 
        response = self.client.get(f"/arama?q={query}")
        assert response.status_code == 200, f"Search failed with status {response.status_code}"

    @task
    def search_empty_query(self):
        response = self.client.get("/arama?q=")
        assert response.status_code == 200, f"Empty search failed with status {response.status_code}"

    @task
    def search_non_existent_product(self):
        query = "NonExistentProduct123"
        response = self.client.get(f"/arama?q={query}")
        assert response.status_code == 200, f"Search for non-existent product failed with status {response.status_code}"

    @task
    def search_multiple_products(self):
        products = ["Smartphone", "Headphones", "Tablet"]
        for product in products:
            response = self.client.get(f"/arama?q={product}")
            assert response.status_code == 200, f"Search for {product} failed with status {response.status_code}"