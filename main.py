import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar ubicaciones al grafo
locations = {
    "A0": (0, 0),
    "S1": (1, 1),
    "S2": (1, 2),
    "S3": (1, 3),
    "S4": (1, 4),
    "S5": (1, 5),
    "S6_1": (1, 6),
    "S6_2": (1,7),
    "S7": (2, 7),
    "S8": (5, 7),
    "S9": (3, 6),
    "P1": (0, 1),
    "P2": (0, 6),
    "P3": (0, 7),
    "P4": (0, 8),
    "P5": (1, 8),
    "P6": (4, 8),
    "P7": (4, 7),
    "P8": (4, 6),
    "P9": (4, 5),
    "P10": (4, 4),
    # Agrega más ubicaciones según sea necesario
}

for location, coordinates in locations.items():
    G.add_node(location, pos=coordinates)

# Agregar conexiones entre ubicaciones
connections = [
    ("A0", "P1"),
    ("P1", "A0"),
    ("P1", "S1"),
    ("S1", "P1"),
    ("P1", "P2"),
    ("S1", "S2"),
    ("S2", "S3"),
    ("S3", "S4"),
    ("S4", "S5"),
    ("S5", "S6_1"),
    ("S6_1", "P2"),
    # Agrega más conexiones según sea necesario
]

G.add_edges_from(connections)


pos = nx.get_node_attributes(G, "pos")
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color="black", font_weight="bold")
plt.title("Mapa de Ubicaciones")

shortest_path = nx.shortest_path(G, source="A0", target="S6_1", weight=None)
print("Ruta más corta:", shortest_path)

plt.show()
