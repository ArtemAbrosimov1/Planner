from locust import HttpUser, task, between
import random

class SupabaseUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.groups = list(range(1, 100))
    
    @task(3)
    def get_group_schedule(self):
        group_id = random.choice(self.groups)
        self.client.get(
            f"/rest/v1/schedule?group_id=eq.{group_id}",
            headers={
                "apikey": ""
            }
        )
    
    @task(1)
    def get_faculties(self):
        self.client.get(
            "/rest/v1/faculties",
            headers={
                "apikey": ""
            }
        )
    
    @task(2) 
    def get_groups_by_faculty(self):
        faculty_id = random.randint(1, 10)
        self.client.get(
            f"/rest/v1/groups?faculty_id=eq.{faculty_id}",
            headers={
                "apikey": ""
            }
        )
