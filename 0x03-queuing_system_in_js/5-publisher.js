#!/usr/bin/env node
import { createClient } from 'redis';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) =>
  console.log('Redis client not connected to the server: ', err)
);

function publishMessage (message, time) {
  console.log('About to send MESSAGE');
  setTimeout(() => {
    client.publish('holberton school channel', message);
  }, time);
}
