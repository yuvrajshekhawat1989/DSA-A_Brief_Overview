# DSA-A Brief Overview

## Lecture-1
DSA is all about solving problems. Therefore let's start with one.

### A sorting problem
Suppose you have to line up students in such a way that they all can see morning assembly. You have 5 students (with heights 170,180,165,175,160 cms) for this task. How would you do this?

- This is a classic sorting problem. There are many ways to do this.
- One of them is to go through all students, compare every two that are standing together and at the end we have the one with maximum height standing at last. You do that 4 more times and you have all students lined according to their heights.
> This way of sorting is one of the most fundamental one also called bubble sort.

### About time complexity
What are number of comparisons made in this approach?
Total number of comparisons made were 4+3+2+1 = 10.

Let's generalize this problem a little bit. Suppose there were n students. What would you do now to apply the same bubble sort and what are number of comparisons involved?
- Total comparisons would be (n-1) + (n-2) + ..... + 1 = (n*(n-1))/2 ~ (n<sup>2</sup>)/2. This is time complexity of bubble sort. The input size, as you can guess is size of input in bits. Since each height can be expressed in 32 bits at most the size of input is 32*n (at max). We ignore the constants in our computation and therefore input size is n.
- Total comparisons were nearly (n<sup>2</sup>)/2. Therefore time complexity is O(n<sup>2</sup>). We ignore constants for our computation.
> Actually O(n<sup>2</sup>) (Big O notation) means that time complexity is at most n<sup>2</sup>. The symbol for precisely stating time complexity is Θ. Θ(n<sup>2</sup>) means time complexity is precisely function of n<sup>2</sup>. Therefore O(n<sup>2</sup>) means complexity could be Θ(n) or Θ(1) or Θ(n<sup>1.5</sup>).
> We ignore the constant terms in time complexity, therefore O(10 * n) is same as O(n). The reason for this is we want to see problem computations growing in terms of input size. For example let's say there were twice many = 10 people in bubble sort problem. The number of computations then will be (10 * 9)/2 which is 45. We can see that computations grew 45/10 ~ 4 fold whice is 2<sup>2</sup>. The constant 1/2 cancelled in division.

Key points to note:
- Each operation like comparison, addition, multiplication, subtraction, division takes O(1) time.
- Time complexity is written as function of input size.

### Time for some problems
Q1. There is an array which contains all distinct elements but one duplicate. Find the duplicate number and Give time complexity of your algorithm.
Q2. (Clasic prime) Given a number n. Check if its prime or not?