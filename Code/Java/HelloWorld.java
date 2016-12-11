import java.util.Scanner;
public class HelloWorld{
  public static void main(String[] args){
    System.out.println("Hello World!");
    System.out.print("Enter a word :: ");
    Scanner kb = new Scanner(System.in);
    String word = kb.nextLine();
    System.out.println("You entered :: "+word);
    System.out.println("Good Bye World");
  }
}
