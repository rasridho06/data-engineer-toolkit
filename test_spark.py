import matplotlib.pyplot as plt
import networkx as nx

# Membuat diagram alur (flowchart) untuk memilih struktur data Python
G = nx.DiGraph()

# Node
nodes = {
    "start": "Apakah data\nberupa pasangan kunci-nilai?",
    "dict": "Gunakan Dictionary\n{key: value}",
    "ordered": "Apakah urutan data penting?",
    "immutable": "Apakah data perlu tetap\n(tidak diubah)?",
    "tuple": "Gunakan Tuple ( )",
    "list": "Gunakan List [ ]",
    "unique": "Apakah data harus unik?",
    "set": "Gunakan Set { }",
    "homogen": "Apakah semua elemen\ntipe sama & numerik?",
    "matrix": "Gunakan Matrix\n(NumPy)",
    "array": "Gunakan Array\n(NumPy)"
}

# Tambahkan node ke graph
for k, v in nodes.items():
    G.add_node(k, label=v)

# Edge (alur logika)
edges = [
    ("start", "dict", {"condition": "Ya"}),
    ("start", "ordered", {"condition": "Tidak"}),
    ("ordered", "immutable", {"condition": "Ya"}),
    ("immutable", "tuple", {"condition": "Ya"}),
    ("immutable", "list", {"condition": "Tidak"}),
    ("ordered", "unique", {"condition": "Tidak"}),
    ("unique", "set", {"condition": "Ya"}),
    ("unique", "homogen", {"condition": "Tidak"}),
    ("homogen", "matrix", {"condition": "Ya, 2D"}),
    ("homogen", "array", {"condition": "Ya, 1D"}),
    ("homogen", "list", {"condition": "Tidak"})
]

# Tambahkan edge ke graph
for u, v, attr in edges:
    G.add_edge(u, v, **attr)

# Posisi node
pos = nx.spring_layout(G, seed=42)

# Gambar node
plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=2500, edgecolors="black")
nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, "label"), font_size=9)

# Gambar edge
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=15, edge_color="gray")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "condition"), font_size=8)

plt.axis("off")
plt.title("Flowchart Pemilihan Struktur Data Python", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
