# Tip!

>- ***If you want to use Breadth-first search algorithm instead of Depth-First Search algorithm, you just need to change "StackFrontier" to "QueueFrontier" in line 89 of maze.py.***
>- ***If you want to use greedy best-first search algorithm instead of Depth-First Search algorithm, you need not only replace "Greedy_bestFirstSearch_frontier" with "StackFrontier" but also add self.goal as a parameter to remove function in line 103 of maze.py.***
>- ***If you want to use A* search algorithm instead of Depth-First Search algorithm, you should follow down steps :***
>   - ***First of all change "cost = None" to "cost" in class Node of util.py***
>   - ***then, add "cost = 0" as a parameter of class Node in line 88 of maze.py.***
>   - ***then, change "StackFrontier" to "A_starSearch_frontier" in line 89 of maze.py.***
>   - ***add self.goal as a parameter to remove function in line 103 of maze.py.***
>   - ***finally, add "cost = node.cost + 1" as a parameter of class Node in line 125 of maze.py..***
