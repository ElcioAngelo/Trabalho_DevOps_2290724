# import time 
# import requests

# flask_app_url = 'http://localhost:5000'
# register_user_url = 'http://localhost:5000/alunomodelview/add'
# user_data = {
#     'nome': 'UsuarioTeste',
#     'sobrenome': 'sobreUusarioTeste',
#     'turma': 'TurmaDoUsuarioTeste',
#     'disciplina': 'DisciplinaTeste',
# }

# def is_container_running():
    
#     try:
#         response = requests.get(flask_app_url)
#         if response.status_code == 200:
#             print("Container is up and running!")
#             return True
#         else:
#             print("Container is not running...")
#             return False
#     except requests.exceptions.RequestException as e:
#         print("An error has ocurred while checking container..")
#         return False

# def register_user():
#     try:
#         response = requests.post(register_user_url,user_data)
#         if response.status_code == 200:
#             print("User created with sucess!!")
#             return True
#         else:
#             print("Failed to create User...")
#             return False
#     except requests.exceptions.RequestException as e:
#         print("An error has occurred while creating the user..")
#         return False 
        
        
# def main():
    
#     retries = 5
#     while retries > 0:
#         if is_container_running():
#             register_user()
#             break
#         else:
#             retries -= 1
#             print("Trying again..")
#             time.sleep(5)
#     else:
#         print("Container failed to open.")
        
# if __name__ == "__main__":
#     main()
  
import pytest
import requests
from unittest.mock import patch

def is_server_running(url: str) -> bool:
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
    
def create_user(url: str, nome: str, sobrenome: str, matricula: str, turma: str):
    user_data = {
        "nome": nome,
        "sobrenome": sobrenome,
        "matricula": matricula,
        "turma": turma
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
        "nome": "John",
        "sobrenome": "Doe",
        "disciplinas": "12345",
        "turma": "A1"
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



            
    
        