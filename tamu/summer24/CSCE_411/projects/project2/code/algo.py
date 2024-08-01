import pickle
from typing import List, Set

def label_nodes(adj_list: List[List[int]], k: int) -> List[int]:
    from random import randint
    return [randint(0, k - 1) for _ in range(len(adj_list))]


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
