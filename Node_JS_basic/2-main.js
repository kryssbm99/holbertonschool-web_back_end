const countStudents = require('./2-read_file');


countStudents('database.csv');


try {
  countStudents('nonexistent.csv');
} catch (error) {
  console.log(error.message);
}