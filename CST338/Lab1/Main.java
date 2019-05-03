/** Andrew Bell */
/** String Manipulator */
import java.util.Scanner;
import java.text.DecimalFormat;

public class Main 
{
   final static int MAX_HOURS = 20;
   final static int MIN_HOURS = 12;

   public static void main(String[] args) 
   {
      //set up scanner object
      Scanner keyboard = new Scanner(System.in);

      System.out.print("Please enter your first name: ");
      String firstName = keyboard.next();

      System.out.print("Please enter your last name: ");
      String lastName = keyboard.next();

      String fullName = firstName + " " + lastName;
      //print full name
      System.out.println(fullName);
      //get length using .length
      System.out.println("Name Length is " + fullName.length());
      //print uppercasified and then lowercasified
      System.out.println(fullName.toUpperCase());
      System.out.println(fullName.toLowerCase());
      System.out.println();

      //set up decimal print
      DecimalFormat printDecimal = new DecimalFormat("#0.0");
      System.out.print("How many hours did you work to 3 decimal places");
      System.out.print("(" + MIN_HOURS + "-" + MAX_HOURS + "): ");
      double hoursWorked = keyboard.nextDouble();

      System.out.print("You worked: ");
      System.out.println(printDecimal.format(hoursWorked));
   }
}
