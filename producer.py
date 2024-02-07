from kafka import KafkaProducer
import time


producer = KafkaProducer(
    bootstrap_servers='localhost:9093', 
    value_serializer=lambda v: str(v).encode('utf-8') 
)

# Produce a message to a Kafka topic
topic = 'kafka_topic'
message = 'Hello, Kafka!'

try:
    for i in range(0, 30):
        producer.send(topic, value=f"{message} {i}")
        print(f"{message} {i}")
        time.sleep(5)

    # Close the producer
    producer.close()
    
except Exception as e:
    print(f"Exception : {e}")