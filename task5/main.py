import uuid
import networkx as nx
import matplotlib.pyplot as plt
from colorsys import hsv_to_rgb

increment = 0.54


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = None
        self.id = str(uuid.uuid4())


class Color:
    def __init__(self, hue, saturation=0.5, value=1.0):
        self.hue = hue
        self.saturation = saturation
        self.value = value

    def to_hex(self):
        rgb_color = hsv_to_rgb(self.hue, self.saturation, self.value)
        return "#{:02x}{:02x}{:02x}".format(int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255))


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal_order, traversal_colors, name):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [traversal_colors[node] for node in tree.nodes]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.text(0.6, 0.5, f"{name}", transform=plt.gca(
    ).transAxes, ha='center', fontsize=14)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors)
    plt.show()


plt.show()


def dfs(node, order, colors):
    global increment
    if node is not None:
        order.append(node.id)
        increment += 0.015
        node.color = Color(increment)
        colors[node.id] = node.color.to_hex()

        dfs(node.left, order, colors)
        dfs(node.right, order, colors)


def bfs(root, order, colors):
    global increment
    queue = [(root, increment)]
    visited = set()
    while queue:
        increment += 0.025
        node, current = queue.pop(0)
        if node.id not in visited:
            order.append(node.id)

            node.color = Color(increment)
            colors[node.id] = node.color.to_hex()
            visited.add(node.id)

            if node.left:
                queue.append((node.left, increment))
            if node.right:
                queue.append((node.right, increment))


def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # BFS
    bfs_order = []
    bfs_colors = {}
    bfs(root, bfs_order, bfs_colors)
    draw_tree(root, bfs_order, bfs_colors, "BFS")
    # DFS
    dfs_order = []
    dfs_colors = {}
    dfs(root, dfs_order, dfs_colors)
    draw_tree(root, dfs_order, dfs_colors, 'DFS')


if __name__ == "__main__":
    main()
