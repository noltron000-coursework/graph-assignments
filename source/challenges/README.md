# Challenge Repo
All graphs challenges are located in this repo from the challenges folder.

## Challenge 4
### Knapsack Problem
#### Description:
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

### Cheapest Sub Sandwich
#### Description:

In the **sandwich problem**, we have a foot long sandwich that is worth a certain amount of money. You can also any other size of sandwich in segments of 1". Therefore, any sandwich between 1" and 12" is available for purchase. However, each size also has differing costs. It might be cheaper to purchase a 4" and 8" sandwich than purchase a full 12" sandwich.

For this problem I am going to make up a set of prices.

| size | price |
|------|-------|
| 12"  | $8.00 |
| 11"  | $7.00 |
| 10"  | $6.00 |
| 9"   | ~~$5.50~~ *$4.00* |
| 8"   | $5.25 |
| 7"   | $4.50 |
| 6"   | $3.49 |
| 5"   | $3.00 |
| 4"   | $2.00 |
| 3"   | $1.69 |
| 2"   | $1.00 |
| 1"   | $0.50 |

In order to make this problem make sense, each sub has an unevenly distributed increase in price. For example the difference between a 3" and 4" sub is different than the difference between a 6" and 7". Note that this sandwich shop's prices are purposefully unrealistic and exploitable &mdash; due to the nature of this problem.

Lets say I want to know the best price for each sub size if I were thinking about any combination of smaller subs.

In order to deconstruct this problem, the first thing I want to do is find the cheapest price for a 1" sub. In this case its $0.50.

A 2" sub is just as expensive as 2 1" subs, but we'll have a preference towards unsliced sandwiches if there is no difference in price.

A 3" sub is more interesting, because its price is more expensive than a 1" and a 2". We can slash that price for future reference, remembering that a 1" and 2" is cheaper. A 4" can be constructed by a 3" and a 1", or two 2" sandwiches... however a 4" sub has the same price as either of these choice.

You can tell how the problem leads from here...

#### Steps of Dynamic Programming:
1. define &amp; count subproblems
	- we have to find which combination of sandwiches is cheapest.
1. "guess" solutions, count choices
	- we should start with the smallest size, because it has no other alternative in price.
1. relate subproblem solutions, compute time per subproblem
	- as we solve each sandwich size going up, we can figure out any sandwich size.
1. recurse &amp; memoize
	- memoize better choice up the recursive stack!
1. solve original problem by checking solved subproblems
	- solve all the subproblems until one series of sandwiches stands out as the best price for the size.