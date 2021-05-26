import pika


params = pika.URLParameters(
    'amqps://yqowytwq:SjF3lZFfltErEjLq2T384qkTYub4z4zv@puffin.rmq2.cloudamqp.com/yqowytwq')


conn = pika.BlockingConnection(params)
channel = conn.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main',
                          body="hello from django to main FLASK")
