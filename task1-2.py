import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()

graph = G.add_edges_from([("Індустр.", "Тракт. завод"), ("Тракт. завод", "Масельського"), ("Масельського", "Армійська"), ("Армійська", "Палац Спорту"), ("Палац Спорту", "Турбоатом"), ("Турбоатом", "Завод Малишева"), ("Завод Малишева", "Спортивна"), ("Спортивна", "Пр. Гагаріна"), ("Пр. Гагаріна", "Майдан Конституції"), ("Майдан Конституції", "Цент. ринок"), ("Цент. ринок", "Південний вокзал"), ("Південний вокзал", "Холодна гора"), ("Героїв Праці", "Студентська"), ("Студентська", "Ак. Павлова"), ("Ак. Павлова", "Ак. Барабашова"), ("Ак. Барабашова", "Київська"), ("Київська", "Я. Мудрого"), ("Я. Мудрого", "Університет"), ("Університет", "Іст. музей"), ("Перемога", "Олексіївська"), ("Олексіївська", "23 Серпня"), ("23 Серпня", "Ботсад"), ("Ботсад", "Наукова"), ("Наукова", "Держпром"), ("Держпром", "Арх. Бекетова"), ("Арх. Бекетова", "Захисників України"), ("Захисників України", "Метробудівників"), ("Майдан Конституції", "Іст. музей"), ("Університет", "Держпром"), ("Спортивна", "Метробудівників")], weight = 2)


pos = nx.spring_layout(G)

node_colors = ['red' if node in ["Індустр.", "Тракт. завод", "Масельського", "Армійська", "Палац Спорту", "Турбоатом", "Завод Малишева", "Спортивна", "Пр. Гагаріна", "Майдан Конституції", "Цент. ринок", "Південний вокзал", "Холодна гора"] else 'blue' if node in ["Героїв Праці", "Студентська", "Ак. Павлова", "Ак. Барабашова", "Київська", "Я. Мудрого", "Університет", "Іст. музей"] else 'green' for node in G.nodes()]


nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=200)

plt.show()

number_of_nodes = G.number_of_nodes()
print(f'Кількість странцій у м. Харьків {number_of_nodes}')
number_of_edges = G.number_of_edges()
print(f'Кількість сполучень странцій у м. Харьків {number_of_nodes}')
degree_centrality = nx.degree_centrality(G)
print(f'Ступінь центральності {degree_centrality}')


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

print()  
print(f'Використання алгоритму DFS для знаходження шляхів у графі: {dfs_recursive(G, 'Індустр.')}')
  

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:  
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited  

print()  
print(f'Використання алгоритму BFS для знаходження шляхів у графі: {bfs_iterative(G, 'Індустр.')}')