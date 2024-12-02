import pytest
import requests
from unittest.mock import patch

def is_server_running(url: str) -> bool:
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
    
def create_user(url: str, nome: str, sobrenome: str, disciplinas: str, turma: str,Ra: str):
    user_data = {
        "nome": nome,
        "sobrenome": sobrenome,
        "Ra":Ra,
        "disciplinas": disciplinas,
        "turma": turma,
    }
    response = requests.post(f"{url}/create_user", json=user_data)
    return response.status_code, response.json()  # Assume the response contains status and user data
    



# Test the server availability check
def test_is_server_running():
    url = "http://localhost:5000"  # Use a real test URL or a mock server URL
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        assert is_server_running(url) is True

        mock_get.return_value.status_code = 404
        assert is_server_running(url) is False

# Test creating a new user
def test_create_user():
    url = "http://localhost:5000/alunomodelview/add"
    user_data = {
        "nome": "Testandooo",
        "sobrenome": "teste",
        "Ra": "4412412421412",
        "disciplinas": "testandooo3",
        "turma": "B9"
    }

    with patch("requests.post") as mock_post:
        # Mock successful response
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"id": 1, **user_data}
        
        status_code, response = create_user(url, **user_data)
        assert status_code == 201
        assert response["nome"] == user_data["nome"]
        assert response["sobrenome"] == user_data["sobrenome"]
        assert response["disciplinas"] == user_data["disciplinas"]
        assert response["turma"] == user_data["turma"]

        # Test error response
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {"error": "Invalid data"}
        
        status_code, response = create_user(url, **user_data)
        assert status_code == 400
        assert response["error"] == "Invalid data"



            
    
        