import networkx as nx
import matplotlib.pyplot as plt

#TODO, calcular a matriz de horários vagos de seg/sex e depois criar a matriz com os dias necessários
def find_common_free_slots_matrix(schedules, days_exam):
    """
    Retorna os horários vagos comuns para os dias especificados.

    :param @schedules: Dicionário com os horários dos cursos.
    :param @days_exam: Lista de índices representando os dias a serem considerados (0 - Seg, 1 - Ter, etc.).
    :return: Matriz com horários vagos comuns para os dias especificados.
    """
    common_free_slots = [[1] * 8 for _ in days_exam]

    for timetable in schedules.values():
        for i, day in enumerate(days_exam):
            for j, slot in enumerate(timetable[day]):
                if slot != 0:
                    common_free_slots[i][j] = 0 # ocupado

    return common_free_slots


schedules = {
    "Agro": [
        [4, 4, 1, 1, 0, 5, 2, 2],
        [1, 10, 2, 5, 12, 12, 0, 0],
        [6, 13, 13, 13, 0, 0, 0, 0],
        [14, 14, 3, 9, 11, 80, 0, 0],
        [6, 3, 8, 8, 7, 7, 0, 0],
    ],
    "Informática": [
        [5, 9, 16, 16, 2, 2, 17, 17],
        [10, 3, 1, 1, 4, 4, 11, 0],
        [5, 11, 6, 1, 0, 0, 0, 0],
        [80, 2, 8, 8, 6, 3, 0, 0],
        [7, 7, 19, 19, 20, 20, 20, 20],
    ],
    "Alimentos": [
        [4, 4, 5, 10, 1, 21, 2, 2],
        [22, 22, 5, 6, 1, 1, 0, 0],
        [23, 23, 24, 24, 0, 0, 0, 0],
        [11, 9, 2, 0, 7, 7, 0, 0],
        [26, 26, 81, 6, 3, 3, 8, 8],
    ],
}

students_exam = [
    [1, 2, 3, 5],
    [2, 6],
    [2],
    [1, 2, 4, 6],
]

days_exam = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
result = find_common_free_slots_matrix(schedules, days_exam)

day_names = ["seg", "ter", "qua", "qui", "sex"]
for i, free_slots in enumerate(result):
    print(f"{day_names[days_exam[i]]}: {' '.join(map(str, free_slots))}")

recovery_disciplines = set() # set nao aceita valores duplicados

for disciplines in students_exam:
    recovery_disciplines.update(disciplines)

recovery_disciplines = sorted(recovery_disciplines)

print("Disciplinas na recuperação: ", recovery_disciplines)

G = nx.Graph()

# cada grupo é adicionado como um grafo completo
for group in students_exam:
    G.add_edges_from([(i, j) for i in group for j in group if i != j])

degree_sequence = sorted(G.degree, key = lambda deg: deg[1], reverse=True)

print("[+] Ordenando nós por grau:")
for d in degree_sequence:
    print("\t[-]", d[0], "--->", d[1])

node_groups = {}
used_groups = []

for node, _ in degree_sequence:
    # Horários dos vizinhos
    neighbor_groups = [node_groups.get(neighbor) for neighbor in G.neighbors(node) if neighbor in node_groups]

    # Pegar o primeiro horário disponível
    available_group = next((group for group in range(len(result)) if group not in neighbor_groups), None)

    if available_group is None:
        print(f"O programa excedeu o número de horários permitidos no nó {node}.")
        exit(1)

    node_groups[node] = available_group
    if available_group not in used_groups:
        used_groups.append(available_group)

print("[+] Grupos atribuídos por nó:")
for n,g in node_groups.items():
    print("\t[-]",n,"--->",g)

# Desenhando o grafo
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=[node_groups[node] for node in G.nodes()],
    node_size=1000,
    font_weight="bold",
    cmap=plt.cm.Paired,
)
plt.show()