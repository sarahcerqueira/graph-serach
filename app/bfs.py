from app.graph import *

class  BreadthFirstSearch:
    @staticmethod
    def bfs(graph: Graph, wantedVertex)->list:
        path = []
        vertexNotVisitedYet = []
        vertexVisited = set()
        vertexNotVisitedYet.append(wantedVertex)
        vertexVisited.add(wantedVertex)

        while len(vertexNotVisitedYet) > 0:
            e = vertexNotVisitedYet.pop(0)
            adjacents = graph.adjacents(e)

            for u in adjacents:
                if u not in vertexVisited:
                    vertexVisited.add(u)
                    vertexNotVisitedYet.append(u)
                    path.append(u)

        return path