# spinoza_unfold.py

import matplotlib.pyplot as plt
import networkx as nx
from physis_engine import PhysisNode
from spinoza_rules import rules

seed = PhysisNode(name="Substance", transform=rules["Substance"]["transform"], depth=4)
seed.unfold(rules)
seed.calculate_scores()

def build_graph(node, graph=None, parent=None):
    if graph is None:
        graph = nx.DiGraph()
    label = f"{node.name}\nA={node.adequacy:.2f}\nΔP={node.delta_p:.2f}\nψ={node.psi:.2f}"
    graph.add_node(label, delta_p=node.delta_p, psi=node.psi)
    if parent:
        graph.add_edge(parent, label)
    for child in node.children:
        build_graph(child, graph, label)
    return graph

graph = build_graph(seed)
pos = nx.spring_layout(graph, seed=42)
colors = [data["delta_p"] for _, data in graph.nodes(data=True)]
sizes = [2000 * data["psi"] for _, data in graph.nodes(data=True)]

plt.figure(figsize=(14, 10))
nx.draw(graph, pos, with_labels=True, node_color=colors, node_size=sizes,
        cmap=plt.cm.coolwarm, font_size=8)
plt.title("Spinoza Recursive Universe — Substance Unfolding")
plt.tight_layout()
plt.savefig("spinoza_output.png")
plt.show()
