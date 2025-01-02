import unittest
from app.graph import *
from app.bfs import *

class TestSortAlgorithm(unittest.TestCase):

    def test_bfs(self):
        path = BreadthFirstSearch.bfs(self.__mockGraphA(), "a")
        pathExpected = ['b', 'c', 'd', 'e', 'f', 'g']
        self.assertListEqual(path, pathExpected)

        path = BreadthFirstSearch.bfs(self.__mockGraphB(), "a")
        pathExpected = ['b', 'd', 'f', 'c', 'g', 'e']
        self.assertListEqual(path, pathExpected)


    def __mockGraphA(self) -> Graph:
        g = Graph()
        g.addVertex("a")
        g.addVertex("b")
        g.addVertex("c")
        g.addVertex("d")
        g.addVertex("e")
        g.addVertex("f")
        g.addVertex("g")
        g.addEdge("a", "b", 28)
        g.addEdge("a", "c", 10)
        g.addEdge("c", "f", 25)
        g.addEdge("b", "d", 14)
        g.addEdge("b", "e", 16)
        g.addEdge("d", "f", 24)
        g.addEdge("d", "g", 18)
        g.addEdge("f", "g", 22)
        g.addEdge("g", "e", 12)

        return g

    def __mockGraphB(self) -> Graph:
        g = Graph()
        g.addVertex("a")
        g.addVertex("b")
        g.addVertex("c")
        g.addVertex("d")
        g.addVertex("e")
        g.addVertex("f")
        g.addVertex("g")
        g.addVertex("h")
        g.addEdge("a", "b", 6)
        g.addEdge("a", "c", 4)
        g.addEdge("b", "c", 5)
        g.addEdge("b", "e", 14)
        g.addEdge("b", "h", 10)
        g.addEdge("c", "f", 2)
        g.addEdge("c", "d", 9)
        g.addEdge("e", "h", 3)
        g.addEdge("f", "g", 15)
        g.addEdge("f", "h", 8)

        return g