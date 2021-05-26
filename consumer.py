import pika


params = pika.URLParameters(
    'amqps://yqowytwq:SjF3lZFfltErEjLq2T384qkTYub4z4zv@puffin.rmq2.cloudamqp.com/yqowytwq')


conn = pika.BlockingConnection(params)
channel = conn.channel()


channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)


print('started consuming')

channel.start_consuming()

channel.close()
