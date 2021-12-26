This should probably in blog post form

blah blah blah 

motivation

definition

approach

consequences

definition

blah blah

## Definitions

### Feasibility vs Optimality

### Model


### Decision Variables
Decision variables are unknowns that can take on a specified range of possible values. Think of them as "eventual" decision variables as the solver will do work and eventually decide the variables value.

This is where a lot of the confusion of constraint programming variables arises. When programming 

## Challenges of Constraint Programming

Expressing the problem (well really the solution)
 - How do you turn a problem description into code (decision variables and constraints)?


What challenges did I face?
 - Expressing the problem
    - Understanding the contraints available
    - Syntax (it's weird)
 
    Thankfully, you can ofen break down the problem into several simplier ones.

    Maybe I pose a problem that seems unrealistic for them to solve and show them how to break it down.
    Offer unit tests for each section


## TODO
 - Instructions on setup for Mac
    - Or use docker or something

 - Separate into chapters
 - Maybe move to jupyter notebook / google collab so can be shared easier

 - Answer why. Why would you choose to use constraint programming

 - Top Resources
    - It was very valuable for me watching and attempting to solve problems along with [this video](https://www.youtube.com/watch?v=hod0L0zfnZs)

 - Limitations of OR-Tools
    - Only solves static problems. The problem definition can't change between starting the run and result.
    - No uncertainty. Problems must be well defined, results feasible or unfeasible. 
    - Hard/impossible to apply your knowledge in the search for solution (naive domain reduction, happens in the solver)

 - A few fancy terms and related subjects
    - [Combinatorial Optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization)
        - Tractibility
    - [Space](https://en.wikipedia.org/wiki/Space_(mathematics)), [Domain](https://en.wikipedia.org/wiki/Domain_(mathematical_analysis))
    - [Operations Research](https://en.wikipedia.org/wiki/Operations_research)


# 0: Introduction
todo

Let's say you are given a problem to solve. In the standard programming paradigmn you start with a state and specify steps that get you to a solution for your problem. In constraint programming... it's different.

First, you describe the bounds of your problem (ex: find the minimum temperature is bounded by 0 Kelvin)   
Second, you describe the problem's solution.  
These make up a model. The model is passed to a let a "solver" which looks for solutions




# 1: Standard Programming vs. Constraint Programming


Example: Find the two greatest unique integers in an array:
 - array contains only whole numbers (0, 1, 2, ...)

Standard Programming (pythonish pseudocode)
```
def greatestUniqueInts(array: List[int]) -> (int, int):
    greatest = -1
    second = -1

    for num in array:
        if num > greatest:
            greatest = num

        if num != greatest and num > second:
            second = num

    if greatest == second or second < 0 greatest < 0:
        raise NotSolvableError("crap")

    return greatest, second
```

Constraint Programming
```
def greatestUniqueInts(array: List[int]) -> (int, int):

    model = CP_Model()

    # decision variables
    greatest = model.Int_Var(0, maxint): # domain: values a variable can take on, anything from 0 to infinity
    second = model.Int_Var(0, maxint)

    # constraint: greatest and second must be unique
    model.Add(greatest != second)

    # maximize
    model.Maximize(greatest + second)

    solution = solver.Solve(model)

    if solution:
        return (solution.greatest, solution.second)
    else:
        raise NotSolvableError("crap")




```