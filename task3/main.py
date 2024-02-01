import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


def shortest_path(graph, start):
    dist = {node: float('infinity') for node in graph}
    paths = {node: [] for node in graph}
    dist[start] = 0
    priority_queue = [(0, start, [start])]

    while priority_queue:
        cur_dist, cur_node, cur_path = heapq.heappop(priority_queue)

        if cur_dist > dist[cur_node]:
            continue

        for neighbor, weight in graph[cur_node].items():
            distance = cur_dist + weight['weight']

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                new_path = cur_path + [neighbor]
                paths[neighbor] = new_path
                heapq.heappush(priority_queue, (distance, neighbor, new_path))

    return {"path": paths, "dist": dist}


def print_shortest_path(shortest_paths):
    for obj in shortest_paths:
        print(obj, '=>', shortest_paths[obj], '\n')


def print_shortest_path_lengths(shortest_path_lengths):
    for obj in shortest_path_lengths:
        print(obj, '=>', shortest_path_lengths[obj])


G = nx.Graph(name="Graf")
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H"])
G.add_weighted_edges_from([("A", "C", 1), ("A", "B", 2), ("C", "E", 2),
                           ("B", "D", 3), ("D", "H", 2), (
    "C", "F", 2), ("E", "G", 2)])


index_to_color = {0: 'blue', 1: 'blue', 2: 'blue',
                  3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue'}

for i, node in enumerate(G.nodes()):
    G.nodes[node]['color'] = index_to_color.get(i, 'blue')

# Draw the graph with node colors
pos = nx.fruchterman_reingold_layout(G)
colors = nx.get_node_attributes(G, 'color').values()
nx.draw(G, pos, with_labels=True, node_color=list(colors))
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the plot
plt.text(0.5, 0.005, f"{G.name}", transform=plt.gca(
).transAxes, ha='center', fontsize=14)
plt.show()


shortest_paths = shortest_path(G, 'D')

print("Hайкоротші шляхи від станції 'D' до всіх інших станцій\n")
print_shortest_path(shortest_paths["path"])
print("\n")

print("Довжини найкоротших шляхів від станції 'D' до всіх інших станцій\n")
print_shortest_path_lengths(shortest_paths["dist"])
