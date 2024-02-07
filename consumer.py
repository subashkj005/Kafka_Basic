from kafka import KafkaConsumer

# Configure Kafka consumer
consumer = KafkaConsumer(
    'kafka_topic',  
    bootstrap_servers='localhost:9093',  
    group_id='1',  
    auto_offset_reset='earliest',   # Convert bytes to string
)

# Consume messages from the topic
for message in consumer:
    print(f"Received message: {message.value}")

# Close the consumer
consumer.close()
