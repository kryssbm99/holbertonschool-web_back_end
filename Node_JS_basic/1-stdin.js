// Display initial message
console.log("Welcome to Holberton School, what is your name?");

// Listen for user input from stdin
process.stdin.on('data', (data) => {
  const name = data.toString().trim();  // Get user input and trim any extra spaces/newlines
  // Ensure the output ends with \r for cross-platform consistency
  console.log(`Your name is: ${name}\r`);
  process.stdin.end();  // End the input process
});

// When stdin is closed, display the closing message
process.stdin.on('end', () => {
  console.log("This important software is now closing");
});

