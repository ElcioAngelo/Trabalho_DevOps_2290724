import time 
import requests
flask_app_url = 'http://localhost:5000'
register_user_url = 'http://localhost:5000/alunomodelview/add'
user_data = {
    'nome': 'UsuarioTeste',
    'sobrenome': 'sobreUusarioTeste',
    'turma': 'TurmaDoUsuarioTeste',
    'disciplina': 'DisciplinaTeste',
}

def is_container_running():
    
    try:
        response = requests.get(flask_app_url)
        if response.status_code == 200:
            print("Container is up and running!")
            return True
        else:
            print("Container is not running...")
            return False
    except requests.exceptions.RequestException as e:
        print("An error has ocurred while checking container..")
        return False

def register_user():
    try:
        response = requests.post(register_user_url,user_data)
        if response.status_code == 200:
            print("User created with sucess!!")
            return True
        else:
            print("Failed to create User...")
            return False
    except requests.exceptions.RequestException as e:
        print("An error has occurred while creating the user..")
        return False 
        
        
def main():
    
    retries = 5
    while retries > 0:
        if is_container_running():
            register_user()
            break
        else:
            retries -= 1
            print("Trying again..")
            time.sleep(5)
    else:
        print("Container failed to open.")
        
if __name__ == "__main__":
    main()
    
        
            
    
        