from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('test-topic',
                         bootstrap_servers='localhost:9093',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    print(f"Received message: {message.value}")
