from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Iris Classification API is running" in response.data


def test_predict():
    client = app.test_client()

    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert "prediction" in response.get_json()