## Insertion Sort Algorithm
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

## Working of Insertion Sort
1. The first element in the array is assumed to be sorted. Take the second element and store it separately as key.
 Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.
2. Now, the first two elements are sorted.

    Take the third element and compare it with the elements on the left of it. Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.
### Algorithm 
```
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
```
### Insertion Sort Complexity
<ol>

1.Time Complexities

1.  Best Case Complexity : O(n) When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
2.  Average Case Complexity : O9n^2) It occurs when the elements of an array are in jumbled order (neither ascending nor descending).
3.  Worst Case Complexity:O(n^2) Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs. 

2.Space Complexities

- Space complexity is O(1) because an extra variable key is used.
</ol>

### Insertion Sort Applications

The insertion sort is used when:
<ul>

- the array is has a small number of elements
- there are only a few elements left to be sorted.
</ul>
