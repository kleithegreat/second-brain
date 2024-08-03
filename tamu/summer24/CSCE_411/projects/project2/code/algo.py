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

def process_graph(args: Tuple[List[List[int]], int]) -> Tuple[List[int], float]:
    adj_list, k = args
    labeling = label_nodes(adj_list, k)
    ratio = proximity_ratio_labels(adj_list, k, labeling)
    return labeling, ratio

def max_proximity_ratio_with_solutions(adj_lists: List[List[List[int]]], k_values: List[int]) -> Tuple[float, List[List[int]]]:
    with mp.Pool() as pool:
        results = pool.map(process_graph, zip(adj_lists, k_values))
    max_ratio = max(result[1] for result in results)
    solutions = [result[0] for result in results]
    return max_ratio, solutions

if __name__ == "__main__":
    with open('./tests/Test_Set_Small_AdjLists_of_Trees', 'rb') as f:
        small_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Test_Set_Small_of_k_values', 'rb') as f:
        small_k_values: List[int] = pickle.load(f)

    with open('./tests/Test_Set_Medium_AdjLists_of_Trees', 'rb') as f:
        medium_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Test_Set_Medium_of_k_values', 'rb') as f:
        medium_k_values: List[int] = pickle.load(f)

    with open('./tests/Test_Set_Large_AdjLists_of_Trees', 'rb') as f:
        large_adj_lists: List[List[List[int]]] = pickle.load(f)

    with open('./tests/Test_Set_Large_of_k_values', 'rb') as f:
        large_k_values: List[int] = pickle.load(f)

    print("Processing and saving solutions...")

    small_max_ratio, small_solutions = max_proximity_ratio_with_solutions(small_adj_lists, small_k_values)
    with open('small_solutions.pkl', 'wb') as f:
        pickle.dump(small_solutions, f)
    print(f"Small Examples: {small_max_ratio:.4f}")

    medium_max_ratio, medium_solutions = max_proximity_ratio_with_solutions(medium_adj_lists, medium_k_values)
    with open('medium_solutions.pkl', 'wb') as f:
        pickle.dump(medium_solutions, f)
    print(f"Medium Examples: {medium_max_ratio:.4f}")

    large_max_ratio, large_solutions = max_proximity_ratio_with_solutions(large_adj_lists, large_k_values)
    with open('large_solutions.pkl', 'wb') as f:
        pickle.dump(large_solutions, f)    
    print(f"Large Examples: {large_max_ratio:.4f}")
    
    print("\nSolutions have been saved as 'small_solutions.pkl', 'medium_solutions.pkl', and 'large_solutions.pkl'")
