const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  res.write('This is the list of our students\n');

  countStudents(databasePath)
    .then((studentData) => {
      res.write(studentData);
      res.end();
    })
    .catch((error) => {
      res.write(error.message);
      res.end();
    });
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
