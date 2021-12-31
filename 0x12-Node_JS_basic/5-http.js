const http = require('http');
const countStudents = require('./3-read_file_async');

const host = 'localhost';
const port = 1245;

const requestListener = async (req, res) => {
  switch (req.url) {
    case '/students':
      res.writeHead(200);
      try {
        const { students, fields } = await countStudents(process.argv[2]);
        res.write(`Number of students: ${students.length}\n`);
        for (const student of students) {
          fields.add(student.field);
        }

        for (const field of fields) {
          const data = students
            .filter((s) => s.field === field)
            .map((s) => s.firstname);

          res.write(
            `Number of students in ${field}: ${data.length}. List: ${data.join(
              ', ',
            )}\n`,
          );
        }
        res.end();
      } catch (err) {
        res.end('Error: Cannot load the database');
      }
      break;
    default:
      res.writeHead(200);
      res.end('Hello Holberton School!');
  }
};

const app = http.createServer(requestListener);
app.listen(port, host);

module.exports = app;
