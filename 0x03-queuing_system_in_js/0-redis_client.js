#!/usr/bin/env node

import { createClient } from 'redis';

const client = await createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => console.log('Redis client not connected to the server: ', err))
  .connect();

await client.disconnect();
