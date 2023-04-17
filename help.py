import requests


def test_missing_api_key():
    invalid_headers = {
        "X-RapidAPI-Key": "invalid_key",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }
    response = requests.get(url="https://moviesdatabase.p.rapidapi.com/titles/tt0001922",headers=invalid_headers)

    assert response.status_code == 403
    assert response.elapsed.total_seconds() < 2
    assert response.headers['Content-Type'] == "application/json"
    output = "You are not subscribed to this API"
    data = response.json()
    assert output in data["message"]