function signUpUser(firstName, lastName) {
  // Return a resolved promise with the user's first and last name
  return Promise.resolve({
    firstName,
    lastName,
  });
}

// Export the function as default
export default signUpUser;
