import requests
import json


class APICalls:
    def __init__(self, url, params=None, headers=None):
        self.url = url
        self.params = params
        self.headers = headers

    # GET method
    def get(self, **kwargs):
        response = requests.get(self.url, params=self.params, headers=self.headers, **kwargs)
        return response

    def get_response_code(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.status_code

    def get_content(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.content

    def get_headers(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.headers

    def get_text(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.text

    def get_request(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.request

    def get_json(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.json()

    def get_response_reason(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.reason

    def response_time(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.elapsed.total_seconds()

    def response_type(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        return response.headers['Content-Type']

    def response_body(self):
        response = requests.get(self.url, params=self.params, headers=self.headers)
        data = response.json()
        return data
