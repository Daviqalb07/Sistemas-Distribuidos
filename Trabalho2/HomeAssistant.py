import threading
import pika
import pickle
from threading import Thread


def callback(ch, method, properties, body):
    print(f"[x] mensagem recebida: {pickle.loads(body)}")

def thread(queue: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host= 'localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue= queue)
    channel.basic_consume(queue= queue, on_message_callback= callback, auto_ack= True)
    channel.start_consuming()

temperature_thread = Thread(target= thread, args= ['temperature'])
temperature_thread.start()

humidity_thread = Thread(target= thread, args= ['humidity'])
humidity_thread.start()

luminosity_thread = Thread(target= thread, args= ['luminosity'])
luminosity_thread.start()