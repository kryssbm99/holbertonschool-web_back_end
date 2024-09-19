const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  res.setHeader('Content-Type', 'text/plain');

  if (parsedUrl.pathname === '/') {
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    res.write('This is the list of our students\n');
    const databasePath = process.argv[2];

    countStudents(databasePath)
      .then((studentData) => {
        res.end(studentData);
      })
      .catch(() => {
        res.end('Cannot load the database');
      });
  } else {
    res.end('404 Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
