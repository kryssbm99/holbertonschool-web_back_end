// Export the default function createEmployeesObject
export default function createEmployeesObject(departmentName, employees) {
    // Use computed property names to dynamically set the department name as the key
    // and employees array as the value
    return {
      [departmentName]: employees,
    };
  }
  