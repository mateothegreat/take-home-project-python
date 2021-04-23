from starlette.testclient import TestClient
import json
import pytest
from typing import List

from app import app

client = TestClient(app)


def test_get_patient():
    response = client.get("/patients/", params={"data": "ya2122"})
    assert response.status_code == 200
    
def test_next_patient():
    response = client.get("/patients/next")
    assert response.status_code == 200
    
def test_delete_patient():
    response = client.delete("/patients/", "ya2w122" )
    assert response.status_code == 200

def test_check_if_patient_is_exist():
    patient= [{
            "id": "ya2122",
            "name": "2o32212",
            "age":12,
            "location": {
                "latitude": "454.000",
                "longitude": "343.343"
            },
            "appointmentsAttended": 12,
            "appointmentsMissed": 12,
            "averageReplyTime": 12
            },
            {
            "id": "ya2w122",
            "name": "2ow32212",
            "age":12,
            "location": {
                "latitude": "454.000",
                "longitude": "343.343"
            },
            "appointmentsAttended": 12,
            "appointmentsMissed": 12,
            "averageReplyTime": 12
            }
            ]
    response = client.post("/patients/", params={"data":patient})
    assert response.status_code == 200
    
