from settings import settings
from client import kafka_client
from client import redmine_client

def request(topic, obj):
    
    response = None
    
    if topic == 'create':
        response = redmine_client.post(obj)

    elif topic == 'read':
        response = redmine_client.get(obj['redmine_id'])
    
    elif topic == 'update':
        response = redmine_client.put(obj)
    
    elif topic == 'delete':
        response = redmine_client.delete(obj['redmine_id'])
    
    return response

def send(msg):
    response = request(obj)

    print('producer')

consumer = kafka_client.Consumer(settings.KAFKA_SERVER, settings.KAFKA_CONSUMER_TOPIC)
for message in consumer.get_consumer():
    message = message.value
    print(message)
