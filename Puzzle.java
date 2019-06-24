// Course: CS4242
// Student name: Jackson Emery
// Student ID: 000563974
// Assignment #: #2
// Due Date: 03/05/2019
// Signature: ______________
// Score: ______________
public class Puzzle
{
  public static String[] Puzzle= {"4","1","3","6","2","5","7","_","8"};
  public static String[] Goal= {"1", "2", "3", "4","_", "5", "6","7","8"};

  public static void main(String[] args)
  {
    // print the initial state, and the target state
    System.out.println("Goal:");
    printPuzzle(Goal);
    System.out.println("Puzzle:");
    printPuzzle(Puzzle);

    //preform A* algorithm
    A(Puzzle, Goal);
  }

  //A* Algorithm
  public static void A(String[] Puzzle, String[] Goal)
  {
    int g = 0;
    int count;
    String[] Temp = new String[9];

    //interate through the algorith many times
    //stop when initial equals goal
    while(true)
    {
      count = 0;
      //array to store our f values
      //one for each direction
      int[] fval = {0,0,0,0};
      //increment level
      g++;

      //keep track of our iterations
      System.out.println("Interation:" + g);

      //preform swap up on our Puzzle
      //save the f value for the swapped puzzle
      //reset to the initial Puzzle
      Temp = Puzzle.clone();
      swapUp(Puzzle);
      fval[0] = f(Puzzle, Goal, g);
      Puzzle = Temp;

      //these three do the same thing just
      //down, left, and right
      Temp = Puzzle.clone();
      swapDown(Puzzle);
      fval[1] = f(Puzzle, Goal, g);
      Puzzle = Temp;

      Temp = Puzzle.clone();
      swapLeft(Puzzle);
      fval[2] = f(Puzzle, Goal, g);
      Puzzle = Temp;

      Temp = Puzzle.clone();
      swapRight(Puzzle);
      fval[3] = f(Puzzle, Goal, g);
      Puzzle = Temp;

      //find our optimal f value
      int min = fval[0];
      int index = 0;

      for(int i = 1; i<fval.length;i++)
      {
        if(fval[i] < min)
        {
          min = fval[i];
          index = i;
        }
      }

      //this switch preforms our first swap

      switch(index)
      {
        case 0:
        swapUp(Puzzle);
        printPuzzle(Puzzle);
          break;

        case 1:
        swapDown(Puzzle);
        printPuzzle(Puzzle);
          break;

        case 2:
        swapLeft(Puzzle);
        printPuzzle(Puzzle);
          break;

        case 3:
        swapRight(Puzzle);
        printPuzzle(Puzzle);
          break;

        default:
          break;
      }
      //check for goal
      for(int j=0; j < 9; j++)
      {
        if(Puzzle[j] == Goal[j])
        {
          count++;
        }
      }
      if(count == 9)
      {
        System.out.println("Goal Reached");
        break;
      }
    }
  }

  //function to find f value
  public static int f(String[] Puzzle, String[] Goal, int g)
  {
    return h(Puzzle,Goal) + g;
  }

  //function to find h value
  public static int h(String[] Puzzle, String[] Goal)
  {
    int count = 0;

    for(int i = 0; i < 9; i++)
    {
        if(Puzzle[i] != Goal[i] && Puzzle[i] != "_")
        {
          count++;
        }
    }
    return count;
  }

  //swap up function
  public static void swapUp(String[] Puzzle)
  {
    // find our blank spot at index i
    int blankSpot;
    for(int i = 0;i < Puzzle.length; i++)
    {
      if(Puzzle[i] == "_")
      {
        blankSpot = i;

        //index i error case, return can't swap up
        if(blankSpot == 0 || blankSpot == 1 || blankSpot == 2)
        {}
        //otherwise, preform swap
        else
        {
          swap(Puzzle, blankSpot, blankSpot - 3);
          break;
        }
      }
    }
  }

  //swap down function
  public static void swapDown(String[] Puzzle)
  {
    int blankSpot;
    for(int i = 0;i < Puzzle.length; i++)
    {
      if(Puzzle[i] == "_")
      {
        blankSpot = i;

        if(blankSpot == 6 || blankSpot == 7 || blankSpot == 8)
        {}
        else
        {
          swap(Puzzle, blankSpot, blankSpot + 3);
          break;
        }
      }
    }
  }

  //swap left
  public static void swapLeft(String[] Puzzle)
  {
    int blankSpot;
    for(int i = 0;i < Puzzle.length; i++)
    {
      if(Puzzle[i] == "_")
      {
        blankSpot = i;

        if(blankSpot == 0 || blankSpot == 3 || blankSpot == 6)
        {}
        else
        {
          swap(Puzzle, blankSpot, blankSpot - 1);
          break;
        }
      }
    }
  }

  //swap right
  public static void swapRight(String[] Puzzle)
  {
    int blankSpot;
    for(int i = 0;i < Puzzle.length; i++)
    {
      if(Puzzle[i] == "_")
      {
        blankSpot = i;

        if(blankSpot == 2 || blankSpot == 5 || blankSpot == 8)
        {}
        else
        {
          swap(Puzzle, blankSpot, blankSpot + 1);
          break;
        }
      }
    }
  }

  //swap function to switch two values
  public static void swap(String[] a, int value, int swapee)
  {
    String temp = a[value];
    a[value] = a[swapee];
    a[swapee] = temp;
  }

  //function to print our puzzle
  public static void printPuzzle(String[] Puzzle)
  {
    for(int i = 0; i < Puzzle.length; i++)
    {
      System.out.print(Puzzle[i]);
      if((i+1) % 3 == 0)
      {
      System.out.println();
      }
    }
    System.out.println();
  }
}
