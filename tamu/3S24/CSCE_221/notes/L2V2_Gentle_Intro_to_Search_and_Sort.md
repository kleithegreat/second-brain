# Gentle Introduction to Search and Sort
- Key takeaways from this:
    - Basic anatomy of search
    - Basic anatomy of sort
    - A feel for juding the performance of search and sort algorithms
## Search
- The process of finding an item with *specified properties from a *given collection of items*
	- Examples:
		- Search an array of integers for the number 36
- Basic search - linear search
	- Basic idea - scan the collection from one end looking for the item until you find it.
	- Pseudocode:
        ```
        Algorithm linSearch(A, n, Item)
            Input: Array A of elements
            Output: TRUE if Item is found, FALSE otherwise

            for i = 0 to n-1 do
                if A[i] == Item then
                    return TRUE
                end if
            end for
            return FALSE
        ```
	- What if the array is ordered?
		- Then we stop search once the current array element is greater than Item
		- Early termination
- Binary search - using ordered arrays
	- Start search in the middle
	- Stop if you find the Item, otherwise search left or right of the middle depending on the value of Item
	- Pseudocode:
        ```
        Algorithm binSearch(A, n, Item)
            Input: Ordered array A of n elements where A[i] >= A[i-1]
            Output: TRUE if Item is found, FALSE otherwise

            low = 0
            high = n-1
            while low <= high
                mid = (low + high) / 2
                if A[mid] == Item then
                    return TRUE
                else if A[mid] < Item then
                    low = mid + 1
                else
                    high = mid - 1
                end if
            end while
            return FALSE
        ```
## Algorithm Performance
- Linear search could take $n$ comparisons at worst
- Binary search could take $log_2 n$ comparisons at worst
- This will be formalized later
## Sorting
- The process of converting a list of elements into ascending or descending order
- Main challenge is the program can't "see" the whole list to know where to move elements
- Programs are usually limited to observing or swapping just two elements at a time
- This is where algorithms become important