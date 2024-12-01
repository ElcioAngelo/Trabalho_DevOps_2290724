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
    
import time
import requests


class FlaskApp:
    def __init__(self, flask_app_url: str, register_user_url: str):
        self.flask_app_url = flask_app_url
        self.register_user_url = register_user_url

    def is_container_running(self) -> bool:
        """Check if the Flask container is running."""
        try:
            response = requests.get(self.flask_app_url)
            if response.status_code == 200:
                print("Container is up and running!")
                return True
            else:
                print("Container is not running...")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error checking container: {e}")
            return False

    def register_user(self, user_data: dict) -> bool:
        """Register a user by posting user data to the specified URL."""
        try:
            response = requests.post(self.register_user_url, json=user_data)
            if response.status_code == 200:
                print("User created successfully!")
                return True
            else:
                print("Failed to create user...")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error creating user: {e}")
            return False


def main():
    flask_app_url = 'http://localhost:5000'
    register_user_url = 'http://localhost:5000/alunomodelview/add'
    user_data = {
        'nome': 'UsuarioTeste',
        'sobrenome': 'sobreUusarioTeste',
        'turma': 'TurmaDoUsuarioTeste',
        'disciplina': 'DisciplinaTeste',
    }

    flask_app = FlaskApp(flask_app_url, register_user_url)

    retries = 5
    while retries > 0:
        if flask_app.is_container_running():
            flask_app.register_user(user_data)
            break
        else:
            retries -= 1
            print("Retrying in 5 seconds...")
            time.sleep(5)
    else:
        print("Container failed to start.")


if __name__ == "__main__":
    main()
       
            
    
        