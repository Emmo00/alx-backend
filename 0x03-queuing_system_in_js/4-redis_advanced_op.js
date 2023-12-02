#!/usr/bin/env node
import redis, { createClient } from 'redis';

const client = createClient();
client.on('connect', () =>
  console.log('Redis client connected to the server')
);
client.on('error', (err) =>
  console.log('Redis client not connected to the server: ', err)
);

client.hset('HolbertonSchools', {Portland:50,Seattle: 80, 'New York': 20, Bogota: 20, Cali: 40, Paris: 2}, redis.print)
client.hgetall()
