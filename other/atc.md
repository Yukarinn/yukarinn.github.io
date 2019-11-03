# [difficulty](https://kenkoooo.com/atcoder/#/table/)

### Nov 2
[abc143e-Travel by Car](https://atcoder.jp/contests/abc143/tasks/abc143_e)
- [upsolve](#oct-20)
- int overflow on large inputs, should use long long
- int overflow on MAX_INT addition
- scanf is fast
- i, j, k -> `fw[j][k]=min(fw[j][k], fw[j][i]+fw[i][k])` add one vertex at a time. recompute the min weight path from j to k with i added to the graph.

### Oct 21
[Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
- divide and conquer
- subproblems:
  - move n-1 disks out of the way
  - move n to dest
  - move n-1 disks on top
- from, to, aux
- complexity: geometric power series

### Oct 20
[abc143d-Triangles](https://atcoder.jp/contests/abc143/tasks/abc143_d)
- 3 for loops
- optimization: ++ for each match is slower than one subtraction to calculate the number of matches (whale: why would you add something twice...)

[**abc143e-Travel by Car**](https://atcoder.jp/contests/abc143/tasks/abc143_e)
- [Floyd Warshall](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)

### Oct 18
[abc142d-Disjoint Set of Common Divisors](https://atcoder.jp/contests/abc142/tasks/abc142_d)
- number of prime divisor of gcd(A, B) + 1
- gcd: euclidean algorithm
- O(sqrt(gcd(A, B))) time to find distinct prime divisors

[abc142e-Get Everything](https://atcoder.jp/contests/abc142/tasks/abc142_e)
- bit mask
- greedy
- reasonable big number for impossible combinations (i.e. big enough but doesn't overflow)
- O(2^N * m)
