import { createClient } from 'redis';

// Connect to the Redis server running locally.
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  const ERROR_MESSAGE = `Error: Redis connection to ${error.address}:${error.port} failed - ${error.message}`;
  console.error(`Redis client not connected to the server: ${ERROR_MESSAGE}`);
});
