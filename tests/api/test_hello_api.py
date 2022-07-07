def test_hello_api(client):
    res = client.get("/hello-world")
    assert res.status_code == 200
