import pika
import json


params = pika.URLParameters(
    'amqps://yqowytwq:SjF3lZFfltErEjLq2T384qkTYub4z4zv@puffin.rmq2.cloudamqp.com/yqowytwq')


conn = pika.BlockingConnection(params)
channel = conn.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
