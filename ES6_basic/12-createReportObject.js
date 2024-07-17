// Export the default function createReportObject
export default function createReportObject(employeesList) {
    // Return an object containing allEmployees and getNumberOfDepartments
    return {
      allEmployees: {
        ...employeesList,
      },
      getNumberOfDepartments() {
        // Return the number of departments
        return Object.keys(this.allEmployees).length;
      },
    };
  }
  