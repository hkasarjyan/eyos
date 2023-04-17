import pytest
from pyapi.api import APICalls
from util.conftest import *


class TestAPI:
    url = "https://moviesdatabase.p.rapidapi.com/titles/tt0001922"
    headers = {
        "X-RapidAPI-Key": "4aa73ad810msh0f2c98cad80fef6p1afb4cjsn22b4b03a630d",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    def test_get_method(self):
        api = APICalls(self.url, headers=self.headers)

        assert api.get_response_code() == 200
        assert api.get_response_reason() == "OK"
        assert api.response_time() < 2
        assert api.response_type() == "application/json; charset=utf-8"
        assert api.response_body()["results"]["id"] == "tt0001922"
        # print(api.response_time())
        #assert api.get_text() is not None
        # api.get_content() is not None
        #assert api.get_headers() is not None

    def test_invalid_optional_param(self):
        params = {"invalid_params": 4}
        api = APICalls(self.url, headers=self.headers, params=params)

        assert api.get_response_code() == 200
        assert api.get_response_reason() == "OK"
        assert api.response_time() < 2
        assert api.response_type() == "application/json; charset=utf-8"
        output = "Wrong filter query parameter"
        assert output in api.response_body()["error"]

    def test_wrong_api_key(self):
        invalid_headers = {
        "X-RapidAPI-Key": "invalid_key",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }
        api = APICalls(self.url, headers=invalid_headers)

        output = "You are not subscribed to this API"
        assert output in api.response_body()["message"]
        assert api.response_time() < 2
        assert api.response_type() == "application/json"


    def test_missing_api_key(self):
        api = APICalls(self.url)

        output = "Invalid API key"
        assert output in api.response_body()["message"]
        assert api.response_time() < 2
        assert api.response_type() == "application/json"