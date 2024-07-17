// Export the default function appendToEachArrayValue
export default function appendToEachArrayValue(array, appendString) {
    // Use for...of loop to iterate over the array
    for (let [index, value] of array.entries()) {
      // Concatenate appendString with the current value and assign it back to the array at the current index
      array[index] = appendString + value;
    }
  
    // Return the modified array
    return array;
  }
  