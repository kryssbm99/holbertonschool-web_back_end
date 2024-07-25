import { uploadPhoto, createUser } from './utils';

/**
 * Handles the profile signup by resolving all promises
 * and logging the required information or handling errors
 */
function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const [photoResponse, userResponse] = results;
      console.log(`${photoResponse.body} ${userResponse.firstName} ${userResponse.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
