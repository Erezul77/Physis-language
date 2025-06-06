# soul_merge.py

import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

st.title("🧠 PHYSIS v0.8 — Soul Merge Spiral")
st.subheader("Upload multiple .physis reflections and unify them into one soul tree.")

uploaded_files = st.file_uploader("Upload multiple .physis files", type="physis", accept_multiple_files=True)

if uploaded_files:
    merged_nodes = defaultdict(lambda: {"count": 0, "adequacy": 0.0, "delta_p": 0.0, "psi": 0.0})

    for uploaded_file in uploaded_files:
        data = json.load(uploaded_file)
        for node in data["nodes"]:
            name = node["name"]
            merged_nodes[name]["count"] += 1
            merged_nodes[name]["adequacy"] += node["adequacy"]
            merged_nodes[name]["delta_p"] += node["delta_p"]
            merged_nodes[name]["psi"] += node["psi"]

    for node in merged_nodes.values():
        count = node["count"]
        node["adequacy"] /= count
        node["delta_p"] /= count
        node["psi"] /= count

    G = nx.DiGraph()
    for name, props in merged_nodes.items():
        label = f"{name}\nĀ={props['adequacy']:.2f}\nΣΔP={props['delta_p']:.2f}\nψ={props['psi']:.2f}"
        G.add_node(label, delta_p=props["delta_p"], psi=props["psi"])

    pos = nx.spring_layout(G, seed=42)
    colors = [data["delta_p"] for _, data in G.nodes(data=True)]
    sizes = [2000 * data["psi"] for _, data in G.nodes(data=True)]

    fig, ax = plt.subplots(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=sizes,
            cmap=plt.cm.coolwarm, font_size=8, ax=ax)
    st.pyplot(fig)

    if st.button("💾 Export Soul Tree"):
        export_data = {
            "soul": [
                {
                    "name": name,
                    "adequacy": round(props["adequacy"], 2),
                    "delta_p": round(props["delta_p"], 2),
                    "psi": round(props["psi"], 2)
                } for name, props in merged_nodes.items()
            ]
        }
        st.download_button("Download soul.physis", json.dumps(export_data, indent=2), file_name="soul.physis")
