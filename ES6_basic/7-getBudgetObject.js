// Export the default function getBudgetObject
export default function getBudgetObject(income, gdp, capita) {
    // Use object property value shorthand syntax to create the budget object
    const budget = {
      income,
      gdp,
      capita,
    };
  
    // Return the budget object
    return budget;
  }
  