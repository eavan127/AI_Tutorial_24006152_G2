"""Graph-search algorithms shared by Labs 1-3: BFS, DFS, UCS, GBFS and A*.

A graph is a dictionary ``{state: [(neighbour, cost), ...]}``. Every algorithm
returns the same ``SearchResult`` so that results can be compared in one table.
``expanded`` counts the states whose neighbours were generated; the goal state
itself is not expanded, so a start that equals the goal expands nothing.
 
graph = {
    "KUL": [("AMS", 10236.7), ("HKT", 837.0), ...],
    "AMS": [("KEF", 2295.0), ...],
    ...
}"""

from __future__ import annotations

from collections import deque
# BFS
from dataclasses import asdict, dataclass
from heapq import heappop, heappush
# priority queue, takes the lowest cost option
from math import inf # infinity; used as "no path / cost unknown" // unreachab
from time import perf_counter # a stopwatch for timing each search


@dataclass(frozen=True)
class SearchResult:
    """What every search returns: the path plus the effort spent finding it."""

    found: bool          # did we reach the goal?
    path: list           # e.g. ["KUL", "AMS", "KEF"]
    hops: int            # number of flights = len(path) - 1
    path_cost_km: float  # total distance
    expanded: int        # how many airports we "opened up" to look at their neighbours
    max_frontier: int    # the most airports waiting in line at any one time (memory use)
    runtime_ms: float    # how long it took

    def as_dict(self) -> dict:
        return asdict(self)


# all of these all objects written in functions
# it should show found to open the particulat memory to enter the value inside
def _build_path(parent: dict, goal) -> list:
    """Follow parent links back from the goal to the start."""
    path = []
    state = goal
    while state is not None:
        path.append(state)
        state = parent[state]
    return path[::-1]
    # reverses the list to ["KUL", "AMS", "KEF"]
    # parent is the front, neighbour is the next connection
    # path can be multiple nodes, but the parent only the one previous 

def _path_cost(path: list, graph: dict) -> float:
    """Sum the edge costs along a path (0 for a single-state path)."""
    edges = {state: dict(neighbours) for state, neighbours in graph.items()}
    return sum(edges[a][b] for a, b in zip(path, path[1:]))

"""
edges = {
    "KUL": {"AMS": 10236.7, "HKT": 837.0},
    "AMS": {"KEF": 2295.0}
}
"""

# directly use dataclass build in in python so that we dont need do multiple initialisations
def _result(found, parent, goal, graph, expanded, max_frontier, started) -> SearchResult:
    path = _build_path(parent, goal) if found else []
    cost = _path_cost(path, graph) if found else inf
    runtime_ms = (perf_counter() - started) * 1000
    return SearchResult(found, path, len(path) - 1, cost, expanded, max_frontier, runtime_ms)


def bfs(graph: dict, start, goal) -> SearchResult:
    """Breadth-first search: fewest edges, ignores edge costs."""
    started = perf_counter()
    frontier = deque([start])
    # FIFO, so will use deque
    # frontier is waiting list
    parent = {start: None}
    # the initial position is None, so when we backtrack when we reach None, it should stop
    expanded, max_frontier = 0, 1
    while frontier:
        state = frontier.popleft() 
        if state == goal:
            return _result(True, parent, goal, graph, expanded, max_frontier, started)

        # if it is not a goal, we will expand the neighbour of KUL
        expanded += 1
        for neighbour, _ in graph.get(state, ()):
            if neighbour not in parent:
                # make sure the neighbour is not the one already travelled (parent)
                parent[neighbour] = state
                # only that it will be added into parent 
                frontier.append(neighbour)
                # added inside the waiting list
        max_frontier = max(max_frontier, len(frontier))
    return _result(False, parent, goal, graph, expanded, max_frontier, started)
    # Queue: KUL
# Call KUL. It's not KEF. Its flights go to AMS and HKT, both new, so write them down and add them to the queue.
# → Queue: AMS, HKT
# Call AMS. It's not KEF. Its flight goes to KEF, which is new, so write it down and add it to the queue.
# → Queue: HKT, KEF
# Call HKT. It's not KEF. Its flight goes to AMS, which is already in the notebook, so skip it.
# → Queue: KEF
# Call KEF. That's the goal, so stop.

# Tracing back with the notebook: KEF came from AMS, and AMS came from KUL. Flipped around, the route is KUL → AMS → KEF, which is 2 flights.


def dfs(graph: dict, start, goal) -> SearchResult:
    """Depth-first search: follows the first listed neighbour as deep as it can."""
    started = perf_counter()
    frontier = [start]
    parent = {start: None}
    expanded, max_frontier = 0, 1
    while frontier:
        state = frontier.pop() # pop the right one, if bfs pop the left one
        # last in first out, so pop the right one
        if state == goal:
            return _result(True, parent, goal, graph, expanded, max_frontier, started)
        expanded += 1
        # Pushed in reverse so that the first listed neighbour is popped first.
        for neighbour, _ in reversed(graph.get(state, ())):
            # reverse to take the neighbour, so that when it pop
            # KUL, AMS, KEF 
            # KEF, AMS, KUL, then pop KUL first 
            if neighbour not in parent:
                parent[neighbour] = state
                frontier.append(neighbour)
        max_frontier = max(max_frontier, len(frontier))
    return _result(False, parent, goal, graph, expanded, max_frontier, started)


def best_first(graph: dict, start, goal, heuristic=None, mode: str = "ucs") -> SearchResult:
    """One loop for UCS (priority g), GBFS (priority h) and A* (priority g + h)."""
    if mode not in ("ucs", "gbfs", "astar"):
        raise ValueError("mode must be 'ucs', 'gbfs' or 'astar'")
    for neighbours in graph.values():
        if any(cost < 0 for _, cost in neighbours):
            raise ValueError("edge costs must be non-negative")
    h = heuristic or (lambda state: 0.0)
   # def h(state): return 0.0

    def priority(state, g):
        if mode == "ucs":
            return g
        # cheapest to go (real cost)
        if mode == "gbfs":
            return h(state)
        # cloest to the goal  (estimated cost)
        return g + h(state)
        # best estimated total trip

    started = perf_counter()
    counter = 0                                  # tie-breaker so states are never compared
    frontier = [(priority(start, 0.0), counter, start, 0.0)]
    best_g = {start: 0.0}
    parent = {start: None}
    expanded_states = set()
    max_frontier = 1
    while frontier:
        _, _, state, g = heappop(frontier)
        if state in expanded_states:
            continue                             # an older, costlier entry for this state
        if state == goal:
            return _result(True, parent, goal, graph, len(expanded_states), max_frontier, started)
        expanded_states.add(state)
        for neighbour, cost in graph.get(state, ()):
            new_g = g + cost # gettting the whole cost, but not only thhe lastest node cost
            if neighbour not in expanded_states and new_g < best_g.get(neighbour, inf):
                best_g[neighbour] = new_g
                parent[neighbour] = state
                counter += 1
                heappush(frontier, (priority(neighbour, new_g), counter, neighbour, new_g))
        max_frontier = max(max_frontier, len(frontier))
    return _result(False, parent, goal, graph, len(expanded_states), max_frontier, started)


def ucs(graph: dict, start, goal) -> SearchResult:
    """Uniform-cost search: cheapest path for non-negative edge costs."""
    return best_first(graph, start, goal, mode="ucs")


def gbfs(graph: dict, start, goal, heuristic) -> SearchResult:
    """Greedy best-first search: fastest to run, no optimality guarantee."""
    return best_first(graph, start, goal, heuristic, mode="gbfs")


def astar(graph: dict, start, goal, heuristic) -> SearchResult:
    """A* search: optimal here when the heuristic is consistent."""
    return best_first(graph, start, goal, heuristic, mode="astar")
