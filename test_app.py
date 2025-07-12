from app import app


def test_home():
    response=app.test_client().get("/")
    
    assert response.test_code==200
    assert response.data==b"hello world"