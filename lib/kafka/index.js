const Kafka = require('node-rdkafka');

const producer = new Kafka.Producer({
  'metadata.broker.list': process.env.KAFKA_HOST,
  dr_cb: true
});

module.exports = producer;
