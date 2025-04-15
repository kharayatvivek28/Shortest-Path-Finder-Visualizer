import time
import heapq

def dijkstra(graph, start, end, update_callback=None, delay=0.1):
    distances = {node: float('inf') for node in graph.nodes}
    previous = {node: None for node in graph.nodes}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)

        if update_callback:
            update_callback(visited)
            time.sleep(delay)

        if current_node == end:
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current = end
    while previous[current] is not None:
        path.insert(0, current)
        current = previous[current]
    if path:
        path.insert(0, current)

    return path, visited
