import random

class SAT():

    def __init__(self, puzzle):
        self.variables = set()
        self.clause_list = []
        self.max_iterations = 100 * 1000
        self.current_iterations = 0
        self.threshold = 0.7
        self.assignment = {}

        random.seed(None)

        # Get clauses
        puzzle = open(puzzle + ".cnf", "r")
        for line in puzzle:
            line = line.split()
            clause = []
            for variable in line:
                clause.append(variable)
            self.clause_list.append(clause)

        # Get variables
        for clause in self.clause_list:
            for variable in clause:
                if variable[0] == "-":
                    self.variables.add(variable[1:4])
                else:
                    self.variables.add(variable)
        self.variables = list(self.variables)

        for variable in self.variables:
            self.assignment[variable] = bool(random.getrandbits(1))

        # Consruct starting assignment
        for clause in self.clause_list:
            # Unit clause: must be true. Add to assignment
            if len(clause) == 1:
                variable = clause[0]
                if variable[0] == "-":
                    self.assignment[variable[1:]] = False
                else:
                    self.assignment[variable] = True

    # Function to check if a clause is satisfied
    def clause_satisfied(self, clause, assignment):
        for variable in clause:
            if variable[0] != "-":
                if assignment[variable] == True:
                    return True
            else:
                if assignment[variable[1:]] == False:
                    return True
        return False


    # Function to score the result of flipping a single variable
    def score_flip(self, variable, assignment):

        assignment_copy = assignment.copy()

        # Score changed
        clauses_satisfied = 0
        assignment_copy[variable] = not assignment_copy[variable]
        for clause in self.clause_list:
            if self.clause_satisfied(clause, assignment_copy):
                clauses_satisfied += 1

        return clauses_satisfied

    # Takes best scored variable and flips it
    def flip_best_variable(self, assignment):

        best_score = -1
        best_var = None

        for variable in self.variables:
            score = self.score_flip(variable, assignment)
            if score > best_score:
                best_score = score
                best_var = variable

        assignment[best_var] = not assignment[best_var]

        return assignment

    def WalkSAT(self):

        assignment = self.assignment.copy() # Random assignment initialized in init
        recently_selected_variables = []
        for i in range(self.max_iterations):
            self.current_iterations += 1
            if self.current_iterations % 1000 == 0:
                print(self.current_iterations)
            if self.current_iterations % 2 == 0:
                recently_selected_variables = []

            # Check if all clauses satisfied
            satisfied = True
            for clause in self.clause_list:
                if not self.clause_satisfied(clause, assignment):
                    satisfied = False
                    break
            if satisfied:
                return assignment

            unsatisfied_clauses = []
            for clause in self.clause_list:
                if not self.clause_satisfied(clause, assignment):
                    unsatisfied_clauses.append(clause)

            rand = int(random.uniform(0, len(unsatisfied_clauses) - 0.0001))
            unsatisfied_clause = unsatisfied_clauses[rand]

            # If below threshold, pick variable in unsatisfied clause with best score
            rand = random.uniform(0, 1)
            if rand < self.threshold:
                best_vars = []
                best_score = -1

                for variable in unsatisfied_clause:
                    if variable[0] == "-":
                        variable = variable[1:]
                    score = self.score_flip(variable, assignment)
                    if score > best_score:
                        best_score = score
                        best_vars = [variable]
                    elif score == best_score:
                        best_vars.append(variable)
                rand = int(random.uniform(0, len(best_vars) - 0.0001))
                var = best_vars[rand]

                if var not in recently_selected_variables:
                    assignment[var] = not assignment[var]
                    recently_selected_variables.append(var)

            # If above threshold, pick random variable in unsatisfied clause to flip
            else:
                rand = int(random.uniform(0, len(unsatisfied_clause) - 0.00001))
                to_flip = unsatisfied_clause[rand]
                if to_flip[0] == "-":
                    to_flip = to_flip[1:]
                assignment[to_flip] = not assignment[to_flip]
        return assignment

    def GSAT(self):

        assignment = self.assignment.copy() # Random assignment initialized in init
        for i in range(self.max_iterations):
            self.current_iterations += 1

            # Check if all clauses satisfied
            satisfied = True
            for clause in self.clause_list:
                if not self.clause_satisfied(clause, assignment):
                    satisfied = False
                    break
            if satisfied:
                return assignment

            rand = random.uniform(0, 1)
            if rand < self.threshold:
                assignment = self.flip_best_variable(assignment)
            else:
                rand = int(random.uniform(0, len(self.variables) - 0.0001))
                assignment[self.variables[rand]] = not assignment[self.variables[rand]]
        return assignment

    def write_solution(self):
        print(self.assignment)
        print("Iterations: " + str(self.current_iterations))

    def main(self, solver):

        if solver == "GSAT":
            result = self.GSAT()
            self.assignment = result
        elif solver == "WalkSAT":
            result = self.WalkSAT()
            self.assignment = result
        else:
            result = None
        return result