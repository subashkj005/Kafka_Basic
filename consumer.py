from kafka import KafkaConsumer

# Configure Kafka consumer
consumer = KafkaConsumer(
    'kafka_topic',  # Replace with your Kafka topic
    bootstrap_servers='localhost:9093',  # Replace with your Kafka broker address
    group_id='1',  # Replace with your consumer group ID
    auto_offset_reset='earliest',  # Start consuming from the beginning of the topic
    value_deserializer=lambda x: x.decode('utf-8')  # Convert bytes to string
)

# Consume messages from the topic
for message in consumer:
    print(f"Received message: {message.value}")

# Close the consumer
consumer.close()
