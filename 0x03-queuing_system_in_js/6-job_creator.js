import kue from 'kue'

const obj = {
    phoneNumber: '00000000000',
    message: 'Hello world',
}
const queue = kue.createQueue()

queue.createJob('push_notification_code')