import random

class SAT():

    def __init__(self, puzzle):
        self.variables = set()
        self.clause_list = []
        self.max_iterations = 3000
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

        # Score changed
        clauses_satisfied = 0
        assignment[variable] = not assignment[variable]
        for clause in self.clause_list:
            if self.clause_satisfied(clause, assignment):
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

        return assignment

    def WalkSAT(self):

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
                rand = int(random.uniform(0, len(self.variables)))
                assignment[self.variables[rand]] = not assignment[self.variables[rand]]
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
                rand = int(random.uniform(0, len(self.variables)))
                assignment[self.variables[rand]] = not assignment[self.variables[rand]]
        return assignment

    def write_solution(self):
        print(self.assignment)
        print("Iterations: " + str(self.current_iterations))

    def main(self, solver):

        if solver == "GSAT":
            result = self.GSAT()
            self.assignment = result
        return result