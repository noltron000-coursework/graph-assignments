# Challenge Repo
All graphs challenges are located in this repo from the challenges folder.

## Challenge 5
### *Knapsack Problem*
#### Explaination
<small>Clearly define the problem. Give full credit to any references you use.</small>

The **knapsack problem** has to do with maximizing value while keeping under a threshold of weight.

At first I attempted to solve this problem by organizing everything by maximizing `value÷weight` specifically, and organizing it in that way. However this did not produce the results that I would desire...

Assume we have a bag that can hold `10` weight units. Consider the example where we have three available items:
- a bag of gold, worth 98 and weighing 5 (very high value/weight)
- a bar of silver, worth 100 and weighing 10 (good value/weight)
- a bag of trash, worth 1 and weighing 5 (terrible value/weight)

If we were to organize these items by their value/weight, we must pick the bag of gold first because it has outstanding value. However that takes up `5` of our weight, and we only can fit `5` more into our bag. Unfortunately, the next best thing we can fit is the bag of trash, which has `5` weight but just `1` value. With both of these items, in total, the bag has `99` value and `10` weight &mdash; but that's less than a bar of silver! If we took that bar of silver instead of this, our weight would still be maximized, but the value would be one extra (`100`).

This is why dynamic programming would make sense here. We have to consider the case where items that are not necessarily the *best* are still considered in the program, while making broad strokes about some bad selections overall. This is just a case of finding the best of the best through some smart recursion.

#### Steps of Dynamic Programming:
1. define &amp; count subproblems
	- we have to find the best next item to put in the bag!
1. "guess" solutions, count choices
	- it doesn't matter which item we choose, but once we choose a choice, we have to consider how it limits further choices.
1. relate subproblem solutions, compute time per subproblem
	- we compare that choice with another choice and choose the better choice.
1. recurse &amp; memoize
	- memoize better choice up the recursive stack!
1. solve original problem by checking solved subproblems
	- solve all the subproblems until one series of all the best choice stands out on top.

#### Sources:
- [Wikipedia](https://en.wikipedia.org/wiki/Knapsack_problem)
- [Geeks for Geeks](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)
- [dev.to](https://dev.to/downey/solving-the-knapsack-problem-with-dynamic-programming-4hce)

### 