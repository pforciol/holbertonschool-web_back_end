import { createClient, print } from 'redis';

// Connect to the Redis server running locally.
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  const ERROR_MESSAGE = `Error: Redis connection to ${error.address}:${error.port} failed - ${error.message}`;
  console.error(`Redis client not connected to the server: ${ERROR_MESSAGE}`);
});

const schools = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [school, value] of Object.entries(schools)) {
  client.hset('HolbertonSchools', school, value, print);
}

client.hgetall('HolbertonSchools', (error, reply) => {
  console.log(reply);
});
