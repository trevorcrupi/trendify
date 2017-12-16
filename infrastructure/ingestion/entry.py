from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))

p = Producer({'bootstrap.servers': 'localhost:9092'})

try:
    p.produce('mytopic', 'activty-01198', callback=acked)

except KeyboardInterrupt:
    pass

p.flush(30)
