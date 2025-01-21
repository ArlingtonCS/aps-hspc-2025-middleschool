# Guess Who

You are hosting a party, and there's a mystery guest you’re trying to identify! Each guest has a name and exactly three traits. Your job is to write a program that finds the guest who matches both clues.

The goal is to narrow it down to one guest based on the clues provided. If no one or multiple people match, your program should print "No match found"


# Input

The first line contains a number that represents the number of test cases (up to 10).

For each test case there will be:

 - A line that contains the number of guests at the party.

 - The next lines describe each guest. Each line contains the guest's name and their three traits, separated by spaces (e.g., Alice blonde tall glasses).

 - The last line contains exactly 2 clues, separated by a space (e.g., blonde glasses).

# Output

The output contains a single line with either the name or names of the guests who fit the description or the phrase "No match found".

# Sample Input
```
2
3  
Alice blonde tall glasses  
Bob brown tall hat  
Charlie blonde short glasses  
blonde glasses  
2  
Diana red tall glasses  
Eve blue short hat  
red hat  
```
# Sample Output
```
Alice Charlie
No match found.  
```