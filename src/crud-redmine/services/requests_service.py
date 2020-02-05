from client import redmine_client
from models import redmine_model
from kafka_client.client import Producer
from settings import settings
import json


def post_request(self, msg):

    if msg != None:

        print('inciando post da tarefa {}'.format(str(msg['issue']['subject'])))

        response = redmine_client.post(msg)

        if response.status_code == 201:
            print('post da tarefa {} realizado com sucesso'.format(str(msg['issue']['subject'])))
            
            print('transmitindo response')

            # producer = Producer()

            # producer.send_message(json.loads(response.json()))

            print('transmissão finalizada com sucesso')
            print(response.json())
        else:
            raise Exception('erro ao realizar create {}'.format(response.status_code))

def get_request(self, msg):

    if msg != None:

        redmine_id = str(msg['id'])

        print('inciando get da tarefa {}'.format(redmine_id))

        response = redmine_client.get(redmine_id)

        if response.status_code == 200:
            
            print('get da tarefa {} realizado com sucesso'.format(redmine_id))
            
            print('transmitindo response')

            # producer = Producer()

            # producer.send_message(json.loads(response.json()))
            
            print('transmissão finalizada com sucesso')
            print(response.json())
        else:
            raise Exception('erro ao realizar get {}'.format(response.status_code))

def put_request(self, msg):

    if msg != None:
        
        redmine_id = str(msg['id'])

        print('inciando update da tarefa {}'.format(redmine_id))
        
        response = redmine_client.put(redmine_id, msg)

        if response.status_code == 200:
            
            print('update da tarefa {} realizado com sucesso'.format(redmine_id))

            print('transmitindo response')

            # producer = Producer()

            # producer.send_message({"sucess":True})

            print('transmissão finalizada com sucesso')
            print({"sucess":True})
        else:
            raise Exception('erro ao realizar update {}'.format(response.status_code))

def delete_request(self, msg):

    if msg != None:

        redmine_id = str(msg['id'])

        print('inciando delete da tarefa {}'.format(redmine_id))

        response = redmine_client.delete(redmine_id)

        if response.status_code == 200:
            print('delete realizado com sucesso')

            print('transmitindo response')
            
            # producer = Producer()

            # producer.send_message({"sucess":True})
            
            print('transmissão finalizada com sucesso')
            print({"sucess":True})
        else:
            raise Exception('erro ao realizar delete {}'.format(response.status_code))
