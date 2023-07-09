# Title: Two Sum - Finding Pairs in a Sorted Array

# Problem Statement:
# Given an array of integers, "numbers," that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
#The task is to determine the indices of these two numbers, index1 and index2, where 1 <= index1 < index2 <= numbers.length. 
#The function should return an integer array [index1, index2] of length 2. 
#It is guaranteed that there is exactly one solution, and the same element cannot be used twice.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 0, index2 = 1. We return [0, 1].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [0,2]
# Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 0, index2 = 2. We return [0, 2].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [0,1]
# Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 0, index2 = 1. We return [0, 1].

# Notes:

# You will always be given a valid list of numbers and a valid target.
# The array is sorted in non-decreasing order, which means the numbers are in increasing order, but duplicates may be present.
# You need to find two distinct numbers that add up to the target.
# The indices returned must be in ascending order (index1 < index2).