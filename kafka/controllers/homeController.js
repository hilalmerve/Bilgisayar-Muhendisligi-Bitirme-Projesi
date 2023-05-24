const { Kafka } = require('kafkajs')
const kafka = new Kafka({
  clientId: 'my-app',
  brokers: ['localhost:9092']
})

const producer = kafka.producer()
const consumer = kafka.consumer({ groupId: 'test-group' })

module.exports.home = function(req, res) {
    res.render('home');
}

module.exports.homePost = function(req, res) {
    const run = async () => {
        // Producing
        var inputValue = req.body.button;
        if (inputValue == "Show") {
        await producer.connect()
        await producer.send({
          topic: 'kafka',
          messages: [
            { value:JSON.stringify(req.body.description)},
          ],
        })                                                                                                             
    }

  await consumer.connect()
  await consumer.subscribe({ topic: 'prediction', fromBeginning: false })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        value: message.value.toString(),
      })
      json = message.value
      var obj = JSON.parse(json);
      res.render('home', {name: obj.predEclassnumber});
    },
  })
  console.log(value)
}
run().catch(console.error)
}