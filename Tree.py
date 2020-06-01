def BFS(tree, visited, node):
    visited.append(node)
    queue.append(node)
    while(queue):
        s = queue.pop(0)
        print(s, end = " ")
        for neighbour in tree[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def DFS(tree, visited, node):
    visited.append(node)
    stack.append(node)
    while(stack):
        s = stack.pop()
        print(s, end = " ")
        for neighbour in tree[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)

if __name__ == "__main__":
    visited = []
    visited2 = []
    queue = []
    stack = []
    tree = {
            'A':['B','C'],
            'B':['D','E'],
            'C':['F','G'],
            'D':[],
            'E':[],
            'F':[],
            'G':[]
        }
    BFS(tree, visited, 'A')
    DFS(tree, visited2, 'A')
