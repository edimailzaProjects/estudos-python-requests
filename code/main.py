# Para começar, é preciso executar o comando pip install requests

import requests
import json

class User:
   url = 'https://gorest.co.in/public/v2/users/'
   auth_token = 'meu_token'

   head = {'Authorization': 'Bearer '+ auth_token}

   ##GET

   requisicao_get = requests.get(url)
   print(requisicao_get) # me trará um 200
   print(requisicao_get.json()) # o método .json me trará a resposta no formato .json

   ##POST

   data = {
      'name':'Edi',
      'gender':'female',
      'email':'edi@qa.com',
      'status':'active'
   }

   requisicao_post = requests.post(url, json = data, headers = head)

   print(requisicao_post.status_code)
   print(requisicao_post.json())
   resp = requisicao_post.json()
   print(resp['id'])
   #se o json tivesse vários niveis seria algo como (resp[x]['id']['outro_campo'])
   #onde "x" é o indicie e "outro campo é o campo mais interno"

   identificador = str(resp['id'])

   ##GET pelo id

   requisicao_get_consulta = requests.get(url + identificador, headers = head)
   print(requisicao_get_consulta.json())

   ##PUT

   data = {
      'name':'Eden',
      'gender':'female',
      'email':'edi@qa.com',
      'status':'active'
   }
   requisicao_put = requests.put(url + identificador, json = data,headers = head)

   ##GET pelo id

   requisicao_get_consulta = requests.get(url + identificador, headers = head)
   print(requisicao_get_consulta.json())

   ##DELETE

   requisicao_delete = requests.delete(url + identificador, headers = head)
   print(requisicao_delete.status_code)

