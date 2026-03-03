from locust import HttpUser, task, between

class FlowForgeUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def list_workflows(self): self.client.get("/api/v1/workflows?tenantId=test")

    @task(2)
    def get_task(self): self.client.get("/api/v1/tasks/test-id")

    @task(1)
    def health_check(self): self.client.get("/health")
