import requests
import pycurl
import json
import pytest
from io import BytesIO


class Test_Api_Class():
    #def __init__(self):
     #   pass

    @pytest.mark.parametrize('password',['Vamsi@4593'])
    @pytest.mark.parametrize('username', ['vamsi4593'])
    def test_put_data(self, username, password):
        usr = username
        pwd = password
        token = self.test_get_token(usr, pwd)
        token_header = token
        assert token_header != "null"

        url = "http://localhost:8080/api/users/"+usr
        print(url)

        payload = {"firstname": "Test First Name", "lastname": "Test Last Name", "phone": "123456789"}
        headers = {
            'Content-Type': 'application/json',
            'Token': token
        }

        response = requests.put(url, headers=headers, data=json.dumps(payload))
        print(response)
        response_body = json.loads(response.text.encode('utf8'))
        assert response_body['message'] == 'Updated'
        assert response_body['status'] == 'SUCCESS'
        print(response_body)

    @pytest.mark.parametrize('password', ['Vamsi@4593', 'Sai@4593'])
    @pytest.mark.parametrize('username', ['vamsi4593', 'testuser'])
    def test_get_users(self, username, password):
        url = "http://localhost:8080/api/users"
        usr = username
        pwd = password
        token = self.test_get_token(usr, pwd)
        token_header = token
        assert token_header != "null"
        print(token_header)

        #if token_header != "null":
        payload = {"username": usr}
        headers = {
            'Content-Type': 'application/json',
            'Token': token_header
        }

        response = requests.get(url, headers=headers, data=payload)
        response_body = response.json()
        print(response_body['payload'][0])
        print([usr])
        assert response_body['payload'][0] == usr
        assert response_body['status'] == 'SUCCESS'
        #else:
         #   print("Token is Invalid.Check username and password")
          #  assert token_header != "null"

    @pytest.mark.parametrize('password', ['Vamsi@4593'])
    @pytest.mark.parametrize('username', ['vamsi4593'])
    def test_get_user_data(self, username, password):
        url = "http://localhost:8080/api/users/"
        usr = username
        pwd = password
        token = self.test_get_token(usr, pwd)
        token_header = token
        assert token_header != "null"

        url = "http://localhost:8080/api/users/" + usr
        headers = {
            'Content-Type': 'application/json',
            'Token': token
        }

        response = requests.get(url, headers=headers)
        response_body = json.loads(response.text.encode('utf8'))
        assert response_body['message'] == 'retrieval succesful'
        print(response_body['payload'])
        print(response_body['payload']['firstname'])
        assert response_body['payload']['firstname'] == 'Test First Name'
        assert response_body['payload']['lastname'] == 'Test Last Name'
        assert response_body['payload']['phone'] == '123456789'
        assert response_body['status'] == 'SUCCESS'
        print(response.text.encode('utf8'))

    @pytest.mark.skip
    def test_get_token(self, username, password):
        url = "http://localhost:8080/api/auth/token"
        usr = username
        pwd = password
        data = BytesIO()
        crl = pycurl.Curl()
        crl.setopt(crl.URL, url)
        crl.setopt(crl.USERPWD, usr+":"+pwd)
        crl.setopt(crl.WRITEFUNCTION, data.write)
        crl.perform()
        crl.close()
        dict = json.loads(data.getvalue())
        if 'token' in dict.keys():
            print(dict["token"])
            return dict["token"]
        else:
            print("Authentication failed.Check Username and Password")
            return "null"




if __name__ == "__main__":
   test = Test_Api_Class()
   test.test_get_users('vamsi4593', 'Vamsi@4593')
   test.test_put_data('vamsi4593', 'Vamsi@4593')
   test.test_get_user_data('vamsi4593', 'Vamsi@4593')
   test.test_get_token('testuser', 'Sai@4593')
