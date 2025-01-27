import networkx as nx
import matplotlib.pyplot as plt

# find the parent of a node
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent, parent[i])  # Path compression
        return parent[i]

# apply union of two sets
def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        # Union by rank
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Kruskal's Algorithm to find the MST
def kruskal_mst(graph):
    # sort all edges by weight
    edges = list(graph.edges(data=True))
    edges.sort(key=lambda x: x[2]['weight'])

    # initialize disjoint sets
    parent = {}
    rank = {}
    for node in graph.nodes:
        parent[node] = node
        rank[node] = 0

    mst_edges = []  # store edges in the MST
    
    # Initialize the plot
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=12, font_weight="bold")
    
    # Draw edge labels for weights
    edge_labels = {(u, v): f'{data["weight"]}' for u, v, data in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_weight='bold')

    # Process edges one by one
    for u, v, weight in edges:
        # Find roots of the nodes u and v
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If they are not in the same set, add the edge to the MST
        if root_u != root_v:
            mst_edges.append((u, v, weight["weight"]))
            union(parent, rank, root_u, root_v)

            # Redraw the graph with the newly added edge
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], edge_color='r', width=2)

            # Draw updated edge weights after adding the edge
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_weight='bold')
            plt.title(f"Step: {len(mst_edges)} - Added edge ({u}, {v}) with weight {weight['weight']}")
            plt.pause(1)  # Pause to show the edge being added
    
    # Show the final MST
    print("(Kruskal's Algorithm) Minimum Spanning Tree Edges and Weights:")
    for u, v, weight in mst_edges:
        print(f"Edge: ({u}, {v}), Weight: {weight}")

    plt.show()

# Create a weighted undirected graph using NetworkX
G = nx.Graph()

# Add nodes and edges with weights
edges = [
    ("A", "B", 4), ("A", "C", 3), ("B", "C", 1),
    ("B", "D", 2), ("C", "D", 4), ("C", "E", 5),
    ("D", "E", 6)
]
G.add_weighted_edges_from(edges)

kruskal_mst(G)
