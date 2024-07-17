// Function to get the current year
function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  // Export the default function getBudgetForCurrentYear
  export default function getBudgetForCurrentYear(income, gdp, capita) {
    // Get the current year
    const currentYear = getCurrentYear();
  
    // Create the budget object using computed property names
    const budget = {
      [`income-${currentYear}`]: income,
      [`gdp-${currentYear}`]: gdp,
      [`capita-${currentYear}`]: capita,
    };
  
    // Return the budget object
    return budget;
  }
  