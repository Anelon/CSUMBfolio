/** Andrew Bell */
/** Casino */
import java.util.Scanner;
//import java.text.DecimalFormat;
import java.util.Random;

public class Assig2 {
   final static int MAX_BET = 100;
   final static int MAX_PULLS = 40;
   private static int pullCount = 0;
   //100 percent used for probability
   final static int MAX_ROLL = 8;
   final static int BAR_CHANCE = 4;
   final static int CHERRY_CHANCE = 6;
   final static int SPACE_CHANCE = 7;
   final static int SEVEN_CHANCE = 8;
   //static strings for consistency and so I can't miss spell them later
   final static String BAR_STR = "BAR";
   final static String CHERRY_STR = "cherries";
   final static String SPACE_STR = "(space)";
   final static String SEVEN_STR = "7";
   private static Scanner keyboard = new Scanner(System.in);
   //initalize randomGenerator
   private static Random randomGenerator = new Random();
   private static int[] pullWinnings = new int[MAX_PULLS];

   //prompts user for how much they want to bet 
   public static int getBet() {
      System.out.print("How much would you like to bet (1 - 100) " +
            "or 0 to quit? ");
      int bet = keyboard.nextInt();
      //check if bet is in the right range
      if (bet < 0 || bet > MAX_BET) {
         return getBet();
      } else {
         return bet;
      }
   }
   
   //Gets a string randomly baised on the max roll and the various chances
   static public String randString() {
      int roll = randomGenerator.nextInt(MAX_ROLL);
      //if block for returning string corresponding to the roll
      if (roll < BAR_CHANCE) 
         return BAR_STR;
      else if (roll < CHERRY_CHANCE) 
         return CHERRY_STR;
      else if (roll < SPACE_CHANCE)
         return SPACE_STR;
      else if (roll < SEVEN_CHANCE)
         return SEVEN_STR;
      //should never hit here
      System.out.println("Bad");
      return "";
   }

   //Pulls the lever (randomly assigning the strings values
   public static TripleString pull() {
      TripleString newPull = new TripleString();
      newPull.setString1(randString());
      newPull.setString2(randString());
      newPull.setString3(randString());
      return newPull;
   }

   //Looks at the pull and analizes it to return the apropriate multiplyer
   public static int getPayMultiplier(TripleString thePull) {
      if (thePull.getString1() == CHERRY_STR) {
         if (thePull.getString1() == CHERRY_STR) {
            if (thePull.getString3() == CHERRY_STR) {
               return 30;
            } else {
               return 15;
            }
         } else {
            return 5;
         }
      }
      if (thePull.getString1() == BAR_STR && thePull.getString2() == BAR_STR &&
            thePull.getString3() == BAR_STR) 
         return 50;
      if (thePull.getString1() == SEVEN_STR && 
            thePull.getString2() == SEVEN_STR &&
            thePull.getString3() == SEVEN_STR) 
         return 100;
      return 0;
   }

   //Display function takes in the pull and winnings and
   //prints them to the screen and a nice way.
   public static void display(TripleString thePull, int winnings) {
      System.out.println("whirrrrrr .... and your pull is ....");
      System.out.print("  " + thePull.getString1());
      System.out.print("  " + thePull.getString2());
      System.out.print("  " + thePull.getString3());
      System.out.println();
      if (winnings == 0) 
         System.out.println("Sorry you lose.");
      else
         System.out.println("Congratulations, you win: " + winnings);

      System.out.println();
   }

   //takes winnings and adds it to the total pull winnings
   //reuturns false if there is too many pulls
   public static boolean saveWinnings(int winnings) {
      if (pullCount >= MAX_PULLS) {
         return false;
      }

      pullWinnings[pullCount] = winnings;
      pullCount++;
      return true;
   }

   //stringifies the pull winnings for better printing
   public static String displayWinnings() {
      String winningString = "";
      int totalWinnings = 0;
      for (int i = 0; i < pullCount; i++) {
         winningString += pullWinnings[i] + " ";
         totalWinnings += pullWinnings[i];
      }
      winningString += "\nYour total winnings were: $" + totalWinnings;
      return winningString;
   }

   //MAIN Entrance to the program
   public static void main(String[] args) {
      //get Bet
      int bet = getBet();
      //if first bet is 0 quit immediatly 
      if (bet == 0) System.exit(0);
      //else run the game loop
      while (bet != 0 && pullCount < MAX_PULLS) {
         TripleString thePull = pull();
         //sets winnings to be what the user bets * multiplyer from the pull
         int winnings = bet * getPayMultiplier(thePull);
         display(thePull, winnings);
         saveWinnings(winnings);

         //Get new bet and reset
         bet = getBet();
      }
      System.out.println("Thanks for playing at the Casino!");
      System.out.println(displayWinnings());

   }
}

//Triple Strig class holds the 3 strings of the pulls
class TripleString {
   //max length of the strings to be held by this class
   final static int MAX_LEN = 20;

   private String string1;
   private String string2;
   private String string3;

   //default constructor takes nothing and fills the strings with nothing
   public TripleString() {
      this.string1 = "";
      this.string2 = "";
      this.string3 = "";
   }

   //getters for all of the strings
   public String getString1() {
      return string1;
   }
   public String getString2() {
      return string2;
   }
   public String getString3() {
      return string3;
   }

   //Validates a string returns if it's less than max length
   public boolean validString(String str) {
      return str.length() < MAX_LEN;
   }
   //setters for all of the strings returns if the string was set
   public boolean setString1(String str) {
      if (validString(str)) {
         string1 = str;
         return true;
      }
      return false;
   }
   public boolean setString2(String str) {
      if (validString(str)) {
         string2 = str;
         return true;
      }
      return false;
   }
   public boolean setString3(String str) {
      if (validString(str)) {
         string3 = str;
         return true;
      }
      return false;
   }
}

