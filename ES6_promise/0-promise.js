/**
 * Returns a Promise
 * @returns {Promise}
 */
function getResponseFromAPI() {
  // Returning a new promise
  return new Promise((resolve) => {
    // The executor function inside the promise can have some logic
    // In this case, we're simply resolving the promise
    resolve('Response from API');
  });
}

// Export the function
export default getResponseFromAPI;
