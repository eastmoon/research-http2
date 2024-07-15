from axios import *

def test_answer():
    response = make_request("asset-manifest.json")
    assert response.status_code == 200  # Validation of status code
    assert response.http_version == "HTTP/2" # Validation of http version
