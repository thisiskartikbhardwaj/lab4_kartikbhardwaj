import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Employee {
    private String employeeID;
    private String name;
    private int age;
    private double salary;

    public Employee(String employeeID, String name, int age, double salary) {
        this.employeeID = employeeID;
        this.name = name;
        this.age = age;
        this.salary = salary;
    }

    public String getEmployeeID() {
        return employeeID;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double getSalary() {
        return salary;
    }
}

public class EmployeeTableSort {
    public static void main(String[] args) {
        List<Employee> employees = new ArrayList<>();
        employees.add(new Employee("161E90", "Raman", 41, 56000));
        employees.add(new Employee("161F91", "Himadri", 38, 67500));
        employees.add(new Employee("161F99", "Jaya", 51, 82100));
        employees.add(new Employee("171E20", "Tejas", 30, 55000));
        employees.add(new Employee("171G30", "Ajay", 45, 44000));

        Scanner scanner = new Scanner(System.in);
        System.out.println("Sort the Employee Table by:");
        System.out.println("1. Age");
        System.out.println("2. Name");
        System.out.println("3. Salary");
        System.out.print("Enter your choice (1/2/3): ");
        int choice = scanner.nextInt();

        switch (choice) {
            case 1:
                Collections.sort(employees, Comparator.comparing(Employee::getAge));
                break;
            case 2:
                Collections.sort(employees, Comparator.comparing(Employee::getName));
                break;
            case 3:
                Collections.sort(employees, Comparator.comparing(Employee::getSalary));
                break;
            default:
                System.out.println("Invalid choice. Sorting by default (Employee ID).");
        }

        // Print the table header
        System.out.printf("%-12s%-15s%-6s%-10s%n", "Employee ID", "Name", "Age", "Salary (PM)");

        // Print the sorted data in a table
        for (Employee employee : employees) {
            System.out.printf("%-12s%-15s%-6d%-10.2f%n",
                    employee.getEmployeeID(), employee.getName(), employee.getAge(), employee.getSalary());
        }
    }
}