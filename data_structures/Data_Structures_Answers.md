Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

O(n), because you have to traverse all nodes.

2. What is the space complexity of your `depth_first_for_each` function?

O(n), because it uses a stack. 

3. What is the runtime complexity of your `breadth_first_for_each` method?

O(n), because you have to traverse all nodes.

4. What is the space complexity of your `breadth_first_for_each` method?

O(n), because it uses a queue. 

5. What is the runtime complexity of your `heapsort` function?

O(n log(n)), because the height of a binary tree is log(n), and we have to exchange the root element with the last leaf element and then potentially bring it all the way from the root to the leaf, repeating this step n times.  

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

The space complexity will be O(n) because we are using an array to store our sorted heap.  However, if we were not using a temporary array but rather sorting within the original array, the space complexity would be O(1), because we do not need to use any extra memory to store anything, we are simply swapping positions of elements.  