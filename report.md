<h3> 

  CS76
  
  21F
  
  PA5
  
  Eitan Vilker
  
  
</h3>


### Discussion

I start off by establishing an assignment with every variable set randomly and then the unit clauses set accordingly, because they need no further information.

I implemented GSAT with the help of two functions: clause_satisfied and flip_best_variable. 
The first function takes a clause and checks to see if one of the statements in it is true, 
and is used to determine if the assignment is complete and to add in scoring.
Flip_best_variable takes the variable whose flip results in the highest number of satisfied clauses and is used to determine, unsurprisingly, which variable to flip.
However, in order to avoid getting stuck in loops, occasionally a variable is picked without regard for scoring.

WalkSAT uses a similar structure to GSAT, with a few modifications. First, WalkSAT never looks at satisfied clauses. 
It instead takes a random unsatisfied clause, chosen from a list of all unsatisfied clauses,
and picks the variable in it that yields the best score in a similar manner to flip_best_variable. In order to avoid getting stuck and improve the runtime, I do a number of things. First, I sometimes flip a random value in the unsatisfied clause instead of the best scoring. Second, I keep track of up to 20 variables at a time and make sure not to flip them so as not to get into a loop. Third, I create a list of best scoring variables instead of choosing the first one with the best score, so that I can randomly pick between them, since they are of equal likelihood to be useful.


### Evaluation

My program was able to get GSAT working in acceptable time for the smaller cnfs, and got WalkSAT working for every cnf. WalkSAT gets one_cell in less than 10 iterations, all_cells in about 300, and rows between 400-800. With the larger puzzles, results are much less consistent, with occasional great successes and, unfortunately, occasional excessively long runtimes. In a lucky result, I even solved puzzle1 in 3587 iterations. The next time I tried it, it took 30661 iterations, which shows the very high variance. I think my program may be a little slow to execute, even though it gets a pretty decent iteration count, but there are no benchmarks for time that I have needed to meet. I suspect that the variance and runtime could be greatly improved by adding deterministic steps as a third potential option. I did actually try to make unit clauses unflippable, but it ended up getting me significantly slower results, interestingly.
