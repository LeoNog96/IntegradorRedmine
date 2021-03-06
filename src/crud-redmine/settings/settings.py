import os
import platform
import logging
import datetime


KAFKA_SERVER = '10.30.80.164:9092'
# KAFKA_SERVER = os.environ['KAFKA_SERVER']

# KAFKA_TOPIC = os.environ['KAFKA_TOPIC']

KAFKA_CONSUMER_TOPIC = ('redmine-delete', 'redmine-create', 'redmine-update', 'redmine-read')

REDMINE_URL = 'http://10.30.80.164:6969/'
# REDMINE_URL = os.environ['REDMINE_URL']

REDMINE_TOKEN = 'aW50ZWdyYWRvcjp0ZXN0ZV8xMjM='
# REDMINE_TOKEN = os.environ['REDMINE_TOKEN']

OS = platform.system()

DELIMITER = '/' if OS == 'Linux' else '\\'

PATH_PROJECT = os.path.abspath('.') + DELIMITER

date = datetime.datetime.now()

date = '{}_{}_{}'.format(date.day, date.month, date.year)

os.makedirs(os.path.dirname(PATH_PROJECT+'logs'+DELIMITER+'{}.log'.format(date)), exist_ok=True)

logging.basicConfig(
    filename=PATH_PROJECT+'logs'+DELIMITER+'{}.log'.format(date),
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging
