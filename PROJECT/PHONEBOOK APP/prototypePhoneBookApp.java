import java.util.Scanner;

public class prototypePhoneBookApp {

  public static void main(String... args) {

    displayMenu();
  }

  public static void addContact(String name) {
    System.out.println("Saved successfully...");
  }

    public static void removeContact(String name, String number) {
     System.out.println("Contact removed successfully...");
  }

  public static void findNumber(String number) {
    //System.out.println("Could not find " + name);
  }

  public static void findContactFirstName(String name) {
    //System.out.println("Saved successfully...");
  }
  public static void findContactLastName(String name) {
    //System.out.println("Saved successfully...");
  }
  
  public static void editContact(String name) {
   //System.out.println("Saved successfully...");
  }

  public static void displayMenu() {

    Scanner in = new Scanner(System.in);
    

    String name;
	String number;
    while (true) {
      System.out.println("What would you like to do?");
      System.out.println("1. Add Contact");
      System.out.println("2. Remove contact");
      System.out.println("3. Find Number");
      System.out.println("4. Find contact by first name");
      System.out.println("5. Find contact by last name");
      System.out.println("6. Edit contact");
      System.out.println("7. Exit");

      int choice = in.nextInt();
      in.nextLine();

      switch (choice) {
        case 1:
          System.out.println("Enter first name:");
          name = in.nextLine();
          System.out.println("Enter last name:");
          name = in.nextLine();
          System.out.println("Enter phone no:");
          number = in.nextLine();
          addContact(name);
          break;

        case 2:
         System.out.println("Enter first name:");
          name = in.nextLine();
	 System.out.println("Enter last name:");
          name = in.nextLine();
         System.out.println("Enter phone no:");
          number = in.nextLine();
          removeContact(name, number);
          break;

        case 3:
          //System.out.println(Firstname)
          // in.nextLine

          findNumber(number);
          break;

	case 4:
	  System.out.println("Enter first name: ");
	    name = in.nextLine(); 
	     findContactFirstName(name);   
	  break;  

	case 5:
	  System.out.println("Enter last name: ");
	    name = in.nextLine();    
	     findContactLastName(name); 
	  break;

	case 6:
	  System.out.println("Edit contact: ");
	    name = in.nextLine();   
		editContact(name);  
	  break;

	case 7:
	  System.out.println("Bye.....");
	   name = in.nextLine();    
	  break;

	default:

          break;
}
      
    }
  }
}