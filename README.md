# Rosalind-Challenges
The Rosalind Challenges are computational problems pertaining to bioinformatics.

Information about the problems can be found on http://rosalind.info/problems/list-view/

My Rosalind profile page: http://rosalind.info/users/khoangotran/

Language used: Python 3

Notable problem:

 	25_Genome Assembly as Shortest Superstring.py
  
The premise is simple: return a shortest superstring containing all the given strings, constructed by gluing together longest segments that overlap.

If the given list of string were ordered, such that simply concatenating all strings starting from index 0 to index n (where n is the last index of the list) while removing all overlapping elements in between the strings, the solution would be trivial. However, the catch is that the strings in the list are not ordered. This means there exists one correct order out of (in the test case) 50! = 30414093201713378043612608166064768844377641568960512000000000000 possible arrangements of elements in the list. If we were somehow given the correct order we can simply concatenate all strings starting from 0 to n and remove all overlapping elements in between to get the shortest superstring. 

Due to the colossal amount of test data to process, the brute force approach is out of the question. This problem forces the use of dynamic programming to complete in a reasonable timeframe. Using dynamic programming, I was able to create an algorithm that process 50 strings with around 1,000 characters each (totalling around 50,000 characters) with varying lengths and calculate the answer within seconds. The steps are all explained in the comments of the code.
