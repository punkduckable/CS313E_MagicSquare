"""
File: MagicSquare.py

Description: This code makes 

Student's Name: Robert Stephany

Student's UT EID: rrs2558

Course Name: CS 313E

Unique Number: 85575

Date Created: 09/12/2019

Date Last Modified: 09/12/2019
"""
from math import log, floor


# Populate a 2-D list with numbers from 1 to n2
def make_square(n):
    """ This method makes a magic square of size n. n is assumed to be an odd
    natural number. The magic square is returned. """

    magic_square = [];

    # First, let's initialze the magic_square up such that it is a nxn grid.
    # I will do this by populating the magic_square with zeros (whcich will
    # soon be replaced with the real contents of the square)
    for i in range(n):
        magic_square.append([0]*n);

    # Next, we iteratively populate the square. This uses the algorithm outlined
    # in the problem statement. I do this using two counters, i and j, which
    # keep track of where we are in the square. We start off in the middle of
    # the bottom row.
    i = n-1;
    j = (n-1)//2;
    for k in range(1,n*n+1):
        # populate the i,j cell of the magic_square!
        magic_square[i][j] = k;

        # determine the cell that is down and to the right of the current
        # position (Note: this accounts for wrap around)
        next_i = i+1 if i != n-1 else 0;
        next_j = j+1 if j != n-1 else 0;

        # now, check if the "next"" cell of magic_square is already populated
        # (which happens if it is non-zero)
        if(magic_square[next_i][next_j] != 0):
            # If so, then we need to go decrement j by 1 and leave j alone
            i = i-1 if i != 0 else n-1;
            j = j;
        else:
            # otherwise, move i and j down and to the right.
            i = next_i;
            j = next_j;

    # magic square should now be populated, return!
    return magic_square



# Print the magic square in a neat format where the numbers
# are right justified
def print_square(magic_square):
    """ This method prints out the magic square. Everything is right justified
    so that it looks pretty. """

    n = len(magic_square);
    print("Here is a %d by %d magic square:\n" % (n,n));

    # First, let's figure out how many characters we need to print out the
    # numbers. This is simply the number of digits in the largest number
    # (which is n*n). This is simply the floor of log(n^2)+1.
    width = floor(log(n*n,10)+1);

    # Now, print out the square row-by-row. right justify the output using
    # width.
    for i in range(n):
        for j in range(n):
            print(str(magic_square[i][j]).rjust(width), end = " ");
        print();             # start a new line

    # finish by adding a blank line below the matrix
    print();



# Check that the 2-D list generated is indeed a magic square
def check_square (magic_square):
    """ This method checks that the magic_square is indeed a magic square.
    To do this, I check that each row of magic_square sums to the same value,
    and that the columns of magic_square sum to the same value. If this is the
    case then the sum of the rows, columns, and two diagionals are printed. """

    n = len(magic_square);

    ############################################################################
    # First, check that all each row of magic_square has the same sum.
    # To do this, we first need to determine the sum of the first row.
    row_sum = 0;
    for j in range(n):
        row_sum += magic_square[0][j];

    # If magic_square really is a magic square then each row of magic_square
    # will have the same sum. Let's check that.
    for i in range(n):
        # find the sum of the ith row
        ith_row_sum = 0;
        for j in range(n):
            ith_row_sum += magic_square[i][j];

        # compare it with the row_sum
        if(ith_row_sum != row_sum):
            print("""This is NOT a magic square. The sum of the 0 row of magic_square is %d\n
                  while the sum of the %d row of magic_square is %d""" % (row_sum, i, ith_row_sum));
            return;

    ############################################################################
    # next, let's check that each column of magic_square has the same sum.
    # first, we need to find the sum of the first column
    col_sum = 0;
    for i in range(n):
        col_sum += magic_square[i][0];

    # if magic_square really is a magic square then each column of magic_square
    # will have the same sum. Let's check that
    for j in range(n):
        # find the sum of the jth column
        jth_col_sum = 0;
        for i in range(n):
            jth_col_sum += magic_square[i][j];

        # compare it with the col_sum
        if(jth_col_sum != row_sum):
            print("""This is NOT a magic square. The sum of the 0 column of magic_square is %d\n
                  while the sum of the %d column of magic_square is %d""" % (col_sum, j, jth_col_sum));
            return;

    ############################################################################
    # If we have made it this far then the rows and columns of magic_square
    # sum to the same value, respectivly. Let's print the row_sum, col_sum
    # and sum of the two diagionals (which we need to calculate)

    main_diagional_sum = 0;
    off_diagional_sum = 0;
    for k in range(n):
        main_diagional_sum += magic_square[k][k];
        off_diagional_sum += magic_square[k][(n-1) - k];

    print("Sum of row = %d" % row_sum);
    print("Sum of column = %d" % col_sum);
    print("Sum diagonal (UL to LR) = %d" % main_diagional_sum);
    print("Sum diagonal (UR to LL) = %d" % main_diagional_sum);



def main():
  # Prompt the user to enter an odd number 3 or greater.
  while True:
      try:
          # First, get input from the user
          n = input("Please enter an odd integer that is 3 or greater: ");

          # Try casting this to an integer. If is not possible, a ValueError
          # will be raised.
          n = int(n);
      except ValueError:
          print("Invalid input. Try again");
          continue;

      # Check the user input

      # if n < 3 then go back to the start
      if(n < 3):
          print("I said 3 or greater (>= 3). Try again.");
          continue;

      # if n is odd then go back to the start
      if(n % 2 == 0):
          print("I said an ODD number. Try again.");
          continue;

      # If we've made it to here then the input satisifes the checks! We can
      # move on!
      break;

  # Create the magic square
  magic_square = make_square(n);

  # Print the magic square
  print_square(magic_square);

  # Verify that it is a magic square
  check_square(magic_square);

main()
