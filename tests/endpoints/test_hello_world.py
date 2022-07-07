from endpoints import hello_world as endpoints


def test_hello():
    assert endpoints.hello() == "Hello World!"
