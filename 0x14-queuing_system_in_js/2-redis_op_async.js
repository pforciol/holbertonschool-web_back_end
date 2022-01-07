import { createClient, print } from 'redis';
import { promisify } from 'util';

// Connect to the Redis server running locally.
const client = createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Set in Redis the value for the key `schoolName`.
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

// Log the value of the key `schoolName` into the console.
const displaySchoolValue = async (schoolName) => {
  console.log(await getAsync(schoolName));
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
