<h3> 

  CS76
  
  21F
  
  PA5
  
  Eitan Vilker
  
  
</h3>


### Discussion

I implemented GSAT with the help of two functions: clause_satisfied and flip_best_variable. 
The first function takes a clause and checks to see if one of the statements in it is true, 
and is used to determine if the assignment is complete and to add in scoring.
Flip_best_variable takes the variable whose flip results in the highest number of satisfied clauses and is used to determine, unsurprisingly, which variable to flip.
However, in order to avoid getting stuck in loops, occasionally a variable is picked without regard for scoring.

WalkSAT uses a similar structure to GSAT, with a few modifications. First, WalkSAT never looks at satisfied clauses. 
It instead takes a random unsatisfied clause, chosen from a list of all unsatisfied clauses,
and picks the variable in it that yields the best score in a similar manner to flip_best_variable. It won't

I made a number of modifications not included in the specifications in order to get a reasonable runtime. First, 


### Evaluation
