from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_ping():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hi Folks": " This is a challenge ApiDocOffice!",
            "Author": "Maprigo",
            "Comments": "I assumed that the doctor had the office at latitude 0 and longitude 0. (to get the distance, I calculate the vector) distance ^ 2 = longitude ^ 2 + latitude ^ 2.",
            "Filters": "The first filter is the attendance ratio,second filter is the distance,third the time of atendance" }