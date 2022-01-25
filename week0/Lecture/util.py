class Node():
    def __init__(self, state, parent, action, cost = None):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Greedy_bestFirstSearch_frontier(StackFrontier):

    def remove(self, maze_goal):
        if self.empty():
            raise Exception("empty frontier")
        else:
            min_Manhattan_distance = []
            remove_node = []
            for node in self.frontier:
                i, j = node.state
                m, n = maze_goal
                Manhattan_distance = abs(m-i) + abs(n-j)
                min_Manhattan_distance.append(Manhattan_distance)
                remove_node.append(node)
            self.frontier.remove(remove_node[min_Manhattan_distance.index(min(min_Manhattan_distance))])
            return remove_node[min_Manhattan_distance.index(min(min_Manhattan_distance))]
        
class A_starSearch_frontier(StackFrontier):

    def remove(self, maze_goal):
        if self.empty():
            raise Exception("empty frontier")
        else:
            min_Manhattan_distance_and_cost = []
            remove_node = []
            for node in self.frontier:
                i, j = node.state
                m, n = maze_goal
                Manhattan_distance = abs(m-i) + abs(n-j)
                value = Manhattan_distance + node.cost
                min_Manhattan_distance_and_cost.append(value)
                remove_node.append(node)
            self.frontier.remove(remove_node[min_Manhattan_distance_and_cost.index(min(min_Manhattan_distance_and_cost))])
            return remove_node[min_Manhattan_distance_and_cost.index(min(min_Manhattan_distance_and_cost))]
