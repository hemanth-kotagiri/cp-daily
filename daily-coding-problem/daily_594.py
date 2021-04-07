# Give a matrix, dictionary, find the words available.(No diagonals)
# { 'eat', 'rain', 'in', 'rat' }
#[['e', 'a', 'n'],
# ['t', 't', 'i'],
# ['a', 'r', 'a']]
# return 3 = > 'eat', 'in', and 'rat'



def sol():

    words = input().split()
    n = int(input())
    matrix = [[input().split()] for i in range(n)]
    visited = [[False for i in range(n)] for i in range(3)] 

    # ALGO: DFS from each node and store the results

    return words, matrix, visited


print(sol())
