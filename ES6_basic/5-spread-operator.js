// Export the default function concatArrays
export default function concatArrays(array1, array2, string) {
    // Concatenate array1, array2, and the characters of string into a single array using spread syntax
    return [...array1, ...array2, ...string];
  }
  