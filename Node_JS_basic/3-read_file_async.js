const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        if (lines.length < 2) {
          reject(new Error('Cannot load the database'));
        }

        const students = lines.slice(1);
        const totalStudents = students.length;
        const fields = {};

        students.forEach((line) => {
          const [firstname, , , field] = line.split(',');

          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        let response = `Number of students: ${totalStudents}\n`;

        for (const field in fields) {
          if (Object.prototype.hasOwnProperty.call(fields, field)) {
            const studentsInField = fields[field];
            response += `Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}\n`;
          }
        }

        resolve(response.trim());
      }
    });
  });
}

module.exports = countStudents;
