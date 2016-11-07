# -*- coding: utf-8 -*-

from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    originHeader = {"origin" : "loadtesting"}
    searchTerms = ["random", "visa", "ukti", "setup guide", "how to"]

    @task(1)
    def notFound(self):
        with self.client.get("/does_not_exist/", headers=self.originHeader, catch_response=True) as response:
          if response.status_code == 404:
            response.success()

    @task(10)
    def searchLanding(self):
        self.client.get("/en/search", headers=self.originHeader,  name='searchLanding')

    @task(10)
    def searchResults(self):
        for s in self.searchTerms:
            self.client.get("/en/results?q=%s" % s, headers=self.originHeader,  name='searchResults')

    @task(50)
    def assets(self):
        self.client.get("/assets/css/main.css", headers=self.originHeader, name='assets')

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # min_wait = 10000
    # max_wait = 11000
