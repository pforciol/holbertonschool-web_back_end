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

// Set in Redis the value for the key `schoolName`.
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (error, reply) => {
    print(`Reply: ${reply}`);
  });
};

// Log the value of the key `schoolName` into the console.
const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
