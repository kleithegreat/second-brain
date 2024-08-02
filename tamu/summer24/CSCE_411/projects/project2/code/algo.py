import pickle
import random
from typing import List, Set, Dict
from collections import Counter, deque
import math

def bfs(adj_list: List[List[int]], start: int, k: int) -> Dict[int, int]:
    distances = {start: 0}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if len(distances) == k:
            break
        for neighbor in adj_list[node]:
            if neighbor not in distances:
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    return distances

def calculate_proximity_ratios(adj_list: List[List[int]], k: int, labeling: List[int]) -> Dict[int, float]:
    ratios = {}
    for v in range(len(adj_list)):
        distances = bfs(adj_list, v, k)
        r_v = float('inf')
        m_v = float('inf')
        for dist in sorted(set(distances.values())):
            labels_within_dist = set(labeling[n] for n in distances if distances[n] <= dist)
            nodes_within_dist = sum(1 for d in distances.values() if d <= dist)
            if len(labels_within_dist) == k and r_v == float('inf'):
                r_v = dist
            if nodes_within_dist >= k and m_v == float('inf'):
                m_v = dist
            if r_v != float('inf') and m_v != float('inf'):
                break
        ratios[v] = r_v / m_v if m_v != 0 else float('inf')
    return ratios

def initial_labeling(adj_list: List[List[int]], k: int) -> List[int]:
    n = len(adj_list)
    labeling = [-1] * n
    for i in range(n):
        if labeling[i] == -1:
            available_labels = set(range(k)) - set(labeling[j] for j in adj_list[i] if labeling[j] != -1)
            labeling[i] = random.choice(list(available_labels) or list(range(k)))
    return labeling

def improve_labeling(adj_list: List[List[int]], k: int, labeling: List[int]) -> List[int]:
    n = len(adj_list)
    max_iterations = n * k  # Set a maximum number of iterations
    for _ in range(max_iterations):
        ratios = calculate_proximity_ratios(adj_list, k, labeling)
        max_ratio = max(ratios.values())
        
        if max_ratio == 1.0:
            break

        worst_nodes = [v for v, r in ratios.items() if r == max_ratio]
        worst_node = random.choice(worst_nodes)
        
        distances = bfs(adj_list, worst_node, k)
        if math.isinf(max_ratio):
            neighborhood = list(distances.keys())
        else:
            neighborhood = [node for node, dist in distances.items() if dist <= int(max_ratio)]
        
        label_counts = Counter(labeling[v] for v in neighborhood)
        
        most_common_label = label_counts.most_common(1)[0][0]
        least_common_label = min(range(k), key=lambda l: label_counts[l])
        
        nodes_with_most_common = [v for v in neighborhood if labeling[v] == most_common_label]
        node_to_swap = max(nodes_with_most_common, key=lambda v: ratios[v])
        
        labeling[node_to_swap] = least_common_label

    return labeling

def label_nodes(adj_list: List[List[int]], k: int, max_attempts: int = 100) -> List[int]:
    best_labeling = None
    best_max_ratio = float('inf')
    for _ in range(max_attempts):
        initial_labels = initial_labeling(adj_list, k)
        final_labeling = improve_labeling(adj_list, k, initial_labels)
        max_ratio = max(calculate_proximity_ratios(adj_list, k, final_labeling).values())
        if max_ratio < best_max_ratio:
            best_labeling = final_labeling
            best_max_ratio = max_ratio
        if max_ratio == 1.0:
            return final_labeling
    return best_labeling


def is_valid(k: int, labeling: List[int]) -> bool:
    return set(labeling) == set(range(k))


def r_v(adj_list: List[List[int]], k: int, labeling: List[int], v: int) -> int:
    r = 0
    Q: List[int] = [v]
    visited: List[bool] = [False] * len(adj_list)
    visited[v] = True
    distinct_labels: Set[int] = {labeling[v]}

    while Q:
        if len(distinct_labels) == k:
            return r
        r += 1
        level_size = len(Q)
        for _ in range(level_size):
            u = Q.pop(0)
            for w in adj_list[u]:
                if not visited[w]:
                    visited[w] = True
                    Q.append(w)
                    distinct_labels.add(labeling[w])
                    if len(distinct_labels) == k:
                        return r
    
    return r

def m_v(adj_list: List[List[int]], k: int, v: int) -> int:
    if k == 1:
        return 0
    
    r = 0
    Q: List[int] = [v]
    visited: List[bool] = [False] * len(adj_list)
    visited[v] = True
    num_visited = 1

    while Q:
        if num_visited >= k:
            return r
        r += 1
        level_size = len(Q)
        for _ in range(level_size):
            u = Q.pop(0)
            for w in adj_list[u]:
                if not visited[w]:
                    visited[w] = True
                    Q.append(w)
                    num_visited += 1
                    if num_visited >= k:
                        return r
    
    return r

def proximity_ratio(adj_list: List[List[int]], k: int, labeling: List[int]) -> float:
    max_r = 0
    for v in range(len(adj_list)):
        ratio = float(r_v(adj_list, k, labeling, v)) / m_v(adj_list, k, v)
        max_r = max(max_r, ratio)
    return max_r

def max_proximity_ratio(adj_lists: List[List[List[int]]], k_values: List[int]) -> float:
    max_ratio = 0
    for adj_list, k in zip(adj_lists, k_values):
        labeling = label_nodes(adj_list, k)
        ratio = proximity_ratio(adj_list, k, labeling)
        max_ratio = max(max_ratio, ratio)
    return max_ratio

def print_comparison(adj_list: List[List[int]], k: int, produced_labeling: List[int], example_labeling: List[int], index: int):
    print(f"Tree {index}:")
    print(f"Number of nodes: {len(adj_list)}")
    print(f"Number of labels (k): {k}")
    print("\nProduced Labeling:")
    print(" ".join(map(str, produced_labeling)))
    print("Example Labeling:")
    print(" ".join(map(str, example_labeling)))
    
    produced_ratio = proximity_ratio(adj_list, k, produced_labeling)
    example_ratio = proximity_ratio(adj_list, k, example_labeling)
    
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
