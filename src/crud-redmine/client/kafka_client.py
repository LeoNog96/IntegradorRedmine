from kafka import KafkaConsumer, KafkaProducer
import json

class Producer:

    producer = None
    producer_topic = None
    
    def __init__(self, server, topic):

        self.producer = KafkaProducer (
            bootstrap_servers=[server],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')                    
        )

        self.producer_topic = topic
    
    def send_message(self, msg):
        producer.send(producer_topic,value=msg)
        producer.flush()

class Consumer:

    __consumer = None
    consumer_topic = None

    def __init__(self, server, topic):

        self.__consumer = KafkaConsumer(
            'kafka-python-topic',
            bootstrap_servers=[server],
            auto_offset_reset='latest',
            enable_auto_commit=True,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
    
    def get_consumer(self):
        return self.__consumer