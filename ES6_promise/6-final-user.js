import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

// Function to handle profile signup
export default function handleProfileSignup(firstName, lastName, fileName) {
  // Call signUpUser and uploadPhoto and handle their promises
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    })));
}
