from kafka_client.client import Consumer
from services.crud_service import Crud
from services.requests_service import *
from settings import settings

class RunService:
    
    logger = None

    def __init__(self):
        self.logger = settings.LOGGER
        self.logger.info('Inicializando Cliente Redmine')
        self.logger.info('Cliente Redmine Iniciado com sucesso')

    def post_receipt(self, msg, topic):
        
        crud = None

        if 'create' in topic:
            self.logger.info('Create')
            crud = Crud(post_request)
        
        elif 'read' in topic:
            self.logger.info('Read')
            crud = Crud(get_request)

        elif 'update' in topic:
            self.logger.info('Update')
            crud = Crud(put_request)

        elif 'delete' in topic:
            self.logger.info('Delete')
            crud = Crud(delete_request)
        
        if crud != None:
            try:
                self.logger.info('Iniciando request')
                crud.request(msg)
            except Exception as ex:
                self.logger.error(str(ex))


    def run(self):
        try:
            self.logger.info("Inicializando conexao com o Servidor do Kafka")
            
            consumer = Consumer(settings.KAFKA_SERVER, settings.KAFKA_CONSUMER_TOPIC)

            self.logger.info("Conectado, aguardando Mensagens")

            for message in consumer.consumer:
                
                self.logger.info("Nova mensagem")
                self.post_receipt(message.value, message.topic)
                # task = threading.Thread(target=self.post_receipt(message.value, message.topic))
                
                # task.start()

        except Exception as exc:
            self.logger.exception(exc)