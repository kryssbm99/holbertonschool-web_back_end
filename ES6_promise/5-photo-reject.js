// Function to upload a photo
export default function uploadPhoto(filename) {
  // Return a rejected promise with the error message
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
