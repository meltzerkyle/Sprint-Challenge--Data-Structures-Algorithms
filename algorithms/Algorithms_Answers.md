Add your answers to the Algorithms exercises here.

I.a) The running time for this would be O(n), insofar as the number of operations needed to satisfy the while loop condition increases with the size of n. 


I.b) The running time for this would be 0(n^4), because the time complexity grows in proportion to the fourth power of the input, given that each loop has n iterations (including the innermost loop, since the size of k is dictated by the size of n as well)  

I.c) Similar to a recursive calculation of Fibonacci numbers, this algorithm is O(2^n), because this algorithm will double with each new element in the input data.


II. For this problem, I would implement a binary tree structure for the algorithm such that we can cut our problem in half based on the outcome of dropping the egg from the middle floor of the building.  Depending if the egg breaks or not when dropped from the middle, we then look at the bottom half or top half of the building exclusively, and then drop from the middle again, dividing the problem in half again and again until we reach our solution. 

