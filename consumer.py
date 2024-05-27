from confluent_kafka import Consumer, KafkaException, KafkaError

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(**conf)

topic = 'test_topic'
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f'{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}')
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(f'Received message: {msg.value().decode("utf-8")}')

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
