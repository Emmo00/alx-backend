#!/usr/bin/env node
import { createClient } from 'redis';

const client = createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) =>
  console.log('Redis client not connected to the server: ', err)
);

client.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubcribe(channel);
    process.exit();
  }
});

client.subscript('holberton school channel');
