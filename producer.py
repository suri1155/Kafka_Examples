from confluent_kafka import Producer
import socket

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

producer = Producer(**conf)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

topic = 'test_topic'

for i in range(10):
    producer.produce(topic, key=str(i), value=f'Suraj here', callback=delivery_report)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is delivered (or failed).
producer.flush()
