from kafka import KafkaProducer
import time

# Configure Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9093',  # Replace with your Kafka broker address
    value_serializer=lambda v: str(v).encode('utf-8')  # Convert values to bytes
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