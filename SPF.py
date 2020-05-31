def SPF(graph,src,dest,visited,distances,predecessors):
    #check if src or dest is in the graph
    if(src not in graph):
        print("src not in graph")
    if(dest not in graph):
        print("dest not in graph")
        
    #check if src is dest
    if src == dest:
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred,None)
        #reverse the list to get it in the right order
        startToEnd = path[0]
        for i in range(1, len(path)):
            startToEnd = path[i] + '---> ' + startToEnd
        print(startToEnd)
    else:
        #make initial cost equal to 0
        if(not visited):
            distances[src] = 0
        #visit the neighbours
        for neighbour in graph[src]:
            if(neighbour not in visited):
                newDistance = distances[src] + graph[src][neighbour]
                if(newDistance < distances.get(neighbour, float('inf'))):
                    distances[neighbour] = newDistance
                    predecessors[neighbour] = src
        #mark src as visited
        visited.append(src)
        unvisited = {}
        #find closest node to src and move to it
        for k in graph:
            if(k not in visited):
                unvisited[k] = distances.get(k,float('inf'))
        newNode = min(unvisited, key = unvisited.get)
        SPF(graph, newNode,'d', visited, distances, predecessors)

if __name__ == "__main__":
    visited =[]
    distances = {}
    predecessors = {}
    graph = {
            's':{'a':2,'b':1},
            'a':{'s':3,'b':4,'c':8},
            'b':{'s':4,'a':2,'d':2},
            'c':{'a':2,'d':7},
            'd':{'b':1,'c':11}
        }
    SPF(graph,'s','d',visited,distances,predecessors)
