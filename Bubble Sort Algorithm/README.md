### Bubble Sort Algorithm
<p>
It is one of the most common sorting algorithm,also known as Exchange Sorting Algorithm.
It compares two adjacent elements and swaps them if they are in the wrong order and repeats the process until the list is sorted. 
</p>

### How Bubble Sort Algorithm works

<ol>
1.At the beginning of the sort it treats the first element of the list as bubble and compares the second element with bubble.
If the second element is smaller than the bubble, it swaps the two. After swapping them the bubble will move to the second element and compare with the third element and the process continues till the last element.

2.The process continues for the remaining iterations. After each iteration, we observe that the largest element present in the sorted array reaches the last index.
</ol>

# Algorithm
```
   begin BubbleSort(list)
   
   for all elements of list
      if list[i] > list[i+1]
         swap(list[i], list[i+1])
      end if
   end for
   
   return list
   
   end BubbleSort
   ```

# Complexity Analysis
For each Iterations it decreases 1 comparision.
<table>

<th>
Iterations 
</th>
<th>
 Number Of Comparisions
</th>
<tr>
<td>
    1st 
</td>

<td>
    n-1
</td>
</tr>

<tr>
<td>
    2nd
</td>

<td>
    n-2
</td>
</tr>

<tr>
<td>
    3rd
</td>

<td>
    n-3
</td>
</tr>
<tr>
<td>
    ....
</td>

<td>
    .....
</td>
</tr>
<tr>
<td>
    n'th 
</td>

<td>
    1
</td>
</tr>

</table>
 So, the total number of comparisions

``` 
(n-1)+(n-2)+(n-3)+.....+1 = n(n-1)/2
equals to n^2 (Approximately)
```

<br>
<ol>

1.Time Complexities

1. Best Case Complexity : The bubble sort algorithm has a best-case time complexity of O(n) for the already sorted array.
2. Average Case Complexity : The average-case time complexity for the bubble sort algorithm is O(n2), which happens when 2 or more elements are in jumbled, i.e., neither in the ascending order nor in the descending order.
3. Worst Case Complexity: The worst-case time complexity is also O(n2), which occurs when we sort the descending order of an array into the ascending order.

2.Space Complexities

- Space complexity is O(1) because an extra variable is used for swapping.

- In the optimized bubble sort algorithm, two extra variables are used. Hence, the space complexity will be O(n^2).
</ol>

# Bubble Sort Applications
Bubble sort is used if
<ul>

- complexity does not matter
-   short and simple code is preferred

</ul>






