import unittest

from data_structures.graph import Graph

class TestGraph(unittest.TestCase):
    """ Tests the Graph class and its member funcs """

    def test_add_node(self):
        """ Tests that add_node properly adds nodes to adjecency list """
        graph = Graph()
        expected_graph = {'a': {'b'}}
        graph.add_node('a', ['b'])
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['a'].add('c')
        graph.add_node('a', 'c')
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['b'] = set({'a', 'd', 'e'})
        graph.add_node('b', ['a', 'd', 'e'])
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['c'] = set('f')
        graph.add_node('c', 'f')
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['d'] = set('b')
        graph.add_node('d', 'b')
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['e'] = set({'b', 'f'})
        graph.add_node('e', 'b')
        graph.add_node('e', 'f')
        self.assertDictEqual(expected_graph, graph._adjecents)

        expected_graph['f'] = set({'c', 'e'})
        graph.add_node('f', 'c')
        graph.add_node('f', 'e')
        self.assertDictEqual(expected_graph, graph._adjecents)

    def test_bfs(self):
        """ Tests that add_node properly adds nodes to adjecency list """
        # Uses graph in this article:
        # http://bit.ly/2ONjp55
        graph = Graph({
            'A': set(['B', 'C']),
            'B': set(['A', 'D', 'E']),
            'C': set(['A', 'F']),
            'D': set(['B']),
            'E': set(['B', 'F']),
            'F': set(['C', 'E'])})
        # self.assertSetEqual(['A', 'B', 'C', ''])
        path = graph.bfs('A')
        self.assertListEqual(['A', 'B', 'C', 'E', 'D', 'F'], path)
        pass