import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Prim's Algorithm
def prim_mst(graph, start_node):
    mst_edges = []  # store the edges of MST
    visited = set([start_node])  # start from any arbitrary node
    edges = list(graph.edges(start_node, data=True))
    
    # Initialize the plot
    plt.figure(figsize=(8, 6))
    
    # Draw the graph with edge labels for weights
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=500, node_color="skyblue", font_size=12, font_weight="bold")
    
    # Draw edge weights on the graph
    edge_labels = {(u, v): f'{data["weight"]}' for u, v, data in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_weight='bold')

    # Keep track of the edges selected for the MST and plot them step by step
    while len(visited) < len(graph.nodes):
        # Find the edge with the minimum weight that connects the visited set with the unvisited nodes
        min_edge = None
        for u, v, weight in edges:
            if u in visited and v not in visited:
                if min_edge is None or weight["weight"] < min_edge[2]["weight"]:
                    min_edge = (u, v, weight)

        # Add the edge to MST and mark the new node as visited
        if min_edge:
            u, v, weight = min_edge
            visited.add(v)
            mst_edges.append((u, v, weight["weight"]))
            
            # Redraw the graph with the newly added edge
            nx.draw_networkx_edges(graph, pos, edgelist=[(u, v)], edge_color='r', width=2)

            # Draw the updated graph with the newly added edge and its weight
            nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_weight='bold')
            plt.title(f"Step: {len(mst_edges)} - Added edge ({u}, {v}) with weight {weight['weight']}")
            plt.pause(1)  # Pause for a moment to visualize the step
            
            # Update the edges list with the new edges connected to the node v
            edges.extend(graph.edges(v, data=True))
    
    # Show the final MST
    print("Minimum Spanning Tree Edges and Weights:")
    for u, v, weight in mst_edges:
        print(f"Edge: ({u}, {v}), Weight: {weight}")

    plt.show()

G = nx.Graph()

# Add nodes and edges with weights
edges = [
    ("A", "B", 4), ("A", "C", 3), ("B", "C", 1),
    ("B", "D", 2), ("C", "D", 4), ("C", "E", 5),
    ("D", "E", 6)
]
G.add_weighted_edges_from(edges)

prim_mst(G, start_node="A")
