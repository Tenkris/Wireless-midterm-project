import pika
import os
import time
import uuid

rabbitmq_host = ''
rabbitmq_queue = 'image_queue'
cur_idx = 1

# Assign a unique publisher ID using uuid
publisher_id = str(uuid.uuid4())

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue=rabbitmq_queue)

def get_latest_image():
    global cur_idx

    file_path = f"/home/viabike/5secImage/output_{cur_idx:03}.jpg"

    if not os.path.exists(file_path):
        print(file_path)
        return None
    
    with open(file_path, 'rb') as img_file:
        image_data = img_file.read()

    return image_data

# publish image to queue
while True:
    image_to_send = get_latest_image()

    if image_to_send is None:
        time.sleep(5)
        continue

    # Publish the message with the publisher's unique ID in the properties
    channel.basic_publish(
        exchange='',
        routing_key=rabbitmq_queue,
        body=image_to_send,
        properties=pika.BasicProperties(
            headers={'publisher_id': publisher_id}  # Adding publisher ID to the message
        )
    )
    print(f"output_{cur_idx:03}.jpg sent to RabbitMQ from publisher {publisher_id}")
    cur_idx += 1
    time.sleep(5)

connection.close()