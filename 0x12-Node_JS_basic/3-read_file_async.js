const fs = require('fs');

const countStudents = async (path) => {
  try {
    const fileContent = await fs.promises.readFile(path, 'utf-8');
    const students = [];
    const lines = fileContent.split(/\r?\n/);
    const keys = lines[0].split(',');

    for (let i = 1; i < lines.length - 1; i += 1) {
      const values = lines[i].split(',');
      const object = {};

      for (let j = 0; j < values.length; j += 1) {
        object[keys[j]] = values[j];
      }
      students.push(object);
    }

    // Display informations.
    console.log(`Number of students: ${students.length}`);
    const fields = new Set();
    for (const student of students) {
      fields.add(student.field);
    }

    for (const f of fields) {
      const data = students
        .filter((s) => s.field === f)
        .map((s) => s.firstname);

      console.log(
        `Number of students in ${f}: ${data.length}. List: ${data.join(', ')}`,
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
