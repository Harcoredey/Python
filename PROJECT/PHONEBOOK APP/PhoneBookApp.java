//Your task is to help Miracle create an app, that will allow him manage his contact. Your app
//must have the following minimum requirement:
//1. Add contact
//2. Remove contact
//3. Find contact by phone number
//4. Find contact by first name
//5. Find contact by last name
//6. Edit contact


import java.util.Scanner;
public class PhoneBookApp {
public static void main(String...args) {

	Scanner input = new Scanner(System.in);

	displayMenu();
	}
	
	//public static void addContact(String name) {
	//System.out.prinln("Add contact" + name);
	}

	//public static void displayMenu() {
	while (true) {	
	System.out.println("What would you like to do?");
	System.out.println("1. Add contact");
	System.out.println("2. Remove contact");
	System.out.println("3. Find contact by phone number");
	System.out.println("4. Find contact by first name");
	System.out.println("5. Find contact by last name");
	System.out.println("6. Edit contact");
	System.out.println("7. Exit");

	int choice = scanner.nextInt();
        scanner.nextLine(); 
	
	switch (choice) {
		case 1:
			System.out.println("Enter first name:");
			String firstName = scanner.nextLine();
			System.out.println("Enter last name:");
			String lastName = scanner.nextLine();
			break;



//System.out.println("Enter first name:");
  //      String firstName = scanner.nextLine();
    //    System.out.println("Enter last name:");
      //  String lastName = scanner.nextLine();
        //System.out.println("Enter PIN:");




}





   }

}