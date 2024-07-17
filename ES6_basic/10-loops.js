// Export the default function appendToEachArrayValue
export default function appendToEachArrayValue(array, appendString) {
    // Use for...of loop to iterate over the array entries
    for (let index in array) {
      // Concatenate appendString with the current value and assign it back to the array at the current index
      array[index] = appendString + array[index];
    }
    // Return the modified array
    return array;
  }
  