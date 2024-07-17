// Export the default function appendToEachArrayValue
export default function appendToEachArrayValue(array, appendString) {
    // Initialize an empty array to store the new values
    const newArray = [];
    
    // Use a for...of loop to iterate over each element in the array
    for (const idx of array) {
      // Append the given string to the current element and push it to the new array
      newArray.push(appendString + idx);
    }
  
    // Return the new array with the modified values
    return newArray;
  }
  