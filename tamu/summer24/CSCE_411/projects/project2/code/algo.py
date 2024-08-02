import pickle
import random
import math
from typing import List, Dict, Tuple
from collections import Counter, deque
from functools import lru_cache
import multiprocessing as mp

@lru_cache(maxsize=None)
def bfs(adj_list: tuple, start: int) -> Dict[int, int]:
    '''Return a dictionary of distances from the start node to all other nodes in the graph.'''
    adj_list = list(adj_list)
    distances = {start: 0}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor not in distances:
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    return distances

def calculate_proximity_ratios(adj_list: List[List[int]], k: int, labeling: List[int]) -> Dict[int, float]:
    '''Return a dictionary of proximity ratios for each node in the graph.'''
    ratios = {}
    adj_tuple = tuple(map(tuple, adj_list))
    for v in range(len(adj_list)):
        distances = bfs(adj_tuple, v)
        r_v = m_v = float('inf')
        for dist in sorted(set(distances.values())):
            labels_within_dist = set(labeling[n] for n in distances if distances[n] <= dist)
            nodes_within_dist = sum(1 for d in distances.values() if d <= dist)
            if len(labels_within_dist) == k and r_v == float('inf'):
                r_v = dist
            if nodes_within_dist >= k and m_v == float('inf'):
                m_v = dist
            if r_v != float('inf') and m_v != float('inf'):
                break
        ratio = r_v / m_v if m_v != 0 else float('inf')
        ratios[v] = ratio
        if ratio == 1.0:
            return ratios
    return ratios

def initial_labeling(adj_list: List[List[int]], k: int) -> List[int]:
    '''Return a random initial labeling of the nodes in the graph.'''
    n = len(adj_list)
    labeling = [-1] * n
    for i in range(n):
        if labeling[i] == -1:
            available_labels = set(range(k)) - set(labeling[j] for j in adj_list[i] if labeling[j] != -1)
            labeling[i] = random.choice(list(available_labels) or list(range(k)))
    return labeling

def improve_labeling(adj_list: List[List[int]], k: int, labeling: List[int]) -> List[int]:
    n = len(adj_list)
    no_improvement_count = 0
    best_max_ratio = float('inf')

    while True:
        ratios = calculate_proximity_ratios(adj_list, k, labeling)
        max_ratio = max(ratios.values())
        
        if max_ratio == 1.0:
            return labeling
        if max_ratio >= best_max_ratio:
            no_improvement_count += 1
        else:
            best_max_ratio = max_ratio
            no_improvement_count = 0
        if no_improvement_count >= n:
            labeling = initial_labeling(adj_list, k)
            best_max_ratio = float('inf')
            no_improvement_count = 0
            continue

        worst_nodes = [v for v, r in ratios.items() if r == max_ratio]
        worst_node = random.choice(worst_nodes)
        distances = bfs(tuple(map(tuple, adj_list)), worst_node)
        neighborhood =list(distances.keys()) if math.isinf(max_ratio) else [node for node, dist in distances.items() if dist <= math.ceil(max_ratio)]
        label_counts = Counter(labeling[v] for v in neighborhood)
        most_common_label = max(range(k), key=lambda l: label_counts[l])
        least_common_label = min(range(k), key=lambda l: label_counts[l])
        nodes_with_most_common = [v for v in neighborhood if labeling[v] == most_common_label]
        node_to_swap = max(nodes_with_most_common, key=lambda v: ratios.get(v, 0))
        labeling[node_to_swap] = least_common_label

def label_nodes(adj_list: List[List[int]], k: int) -> List[int]:
    while True:
        initial_labels = initial_labeling(adj_list, k)
        final_labeling = improve_labeling(adj_list, k, initial_labels)
        max_ratio = max(calculate_proximity_ratios(adj_list, k, final_labeling).values())
        if max_ratio == 1.0:
            return final_labeling

def proximity_ratio_labels(adj_list: List[List[int]], k: int, labeling: List[int]) -> float:
    return max(calculate_proximity_ratios(adj_list, k, labeling).values())

def process_graph(args: Tuple[List[List[int]], int]) -> float:
    adj_list, k = args
    labeling = label_nodes(adj_list, k)
    return proximity_ratio_labels(adj_list, k, labeling)

def max_proximity_ratio(adj_lists: List[List[List[int]]], k_values: List[int]) -> float:
    with mp.Pool() as pool:
        results = pool.map(process_graph, zip(adj_lists, k_values))
    return max(results)

def print_comparison(adj_list: List[List[int]], k: int, produced_labeling: List[int], example_labeling: List[int], index: int):
    print(f"Tree {index}:")
    print(f"Number of nodes: {len(adj_list)}")
    print(f"Number of labels (k): {k}")
    print("\nProduced Labeling:")
    print(" ".join(map(str, produced_labeling)))
    print("Example Labeling:")
    print(" ".join(map(str, example_labeling)))
    
    produced_ratio = proximity_ratio_labels(adj_list, k, produced_labeling)
    example_ratio = proximity_ratio_labels(adj_list, k, example_labeling)
    
    print(f"\nProximity Ratio (Produced): {produced_ratio:.4f}")
    print(f"Proximity Ratio (Example): {example_ratio:.4f}")
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    with open('./tests/Examples_of_AdjLists_of_Trees', 'rb') as f:
        adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Examples_of_k_values', 'rb') as f:
        k_values: List[int] = pickle.load(f)

    with open('./tests/Examples_of_labelling', 'rb') as f:
        example_labelings: List[List[int]] = pickle.load(f)

    with open('./tests/Small_Examples_of_AdjLists_of_Trees', 'rb') as f:
        small_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Small_Examples_of_k_values', 'rb') as f:
        small_k_values: List[int] = pickle.load(f)

    with open('./tests/Medium_Examples_of_AdjLists_of_Trees', 'rb') as f:
        medium_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Medium_Examples_of_k_values', 'rb') as f:
        medium_k_values: List[int] = pickle.load(f)

    with open('./tests/Large_Examples_of_AdjLists_of_Trees', 'rb') as f:
        large_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Large_Examples_of_k_values', 'rb') as f:
        large_k_values: List[int] = pickle.load(f)

    print("Examples:\n")

    for i, (adj_list, k, example_labeling) in enumerate(zip(adj_lists, k_values, example_labelings)):
        produced_labeling = label_nodes(adj_list, k)
        print_comparison(adj_list, k, produced_labeling, example_labeling, i)

    print("Maximum Proximity Ratios:")
    print(f"Small Examples: {max_proximity_ratio(small_adj_lists, small_k_values):.4f}")
    print(f"Medium Examples: {max_proximity_ratio(medium_adj_lists, medium_k_values):.4f}")
    print(f"Large Examples: {max_proximity_ratio(large_adj_lists, large_k_values):.4f}")
