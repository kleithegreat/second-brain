from typing import List, Dict, Any
import pickle

def solve_instance(n: int, P: int, Q: int, k_list: List[int], m_list: List[int], 
                   T_list: List[List[int]], M_list: List[List[int]]) -> List[int]:
    solution: List[bool] = [False] * n

    changed = True
    while changed:
        changed = False

        for i in range(P):
            left_side = all(solution[T_list[i][j]] for j in range(k_list[i]))
            right_side = solution[T_list[i][-1]]

            if left_side and not right_side:
                solution[T_list[i][-1]] = True
                changed = True

        for i in range(Q):
            if all(solution[j] for j in M_list[i]):
                return []
    
    return [int(x) for x in solution]


def solve_all_instances(instances: Dict[str, Any]) -> List[List[int]]:
    solutions: List[List[int]] = []
    for i in range(instances['numInstances']):
        n: int = instances['n_list'][i]
        P: int = instances['P_list'][i]
        Q: int = instances['Q_list'][i]
        k_list: List[int] = instances['k_list'][i]
        m_list: List[int] = instances['m_list'][i]
        T_list: List[List[int]] = instances['T_list'][i]
        M_list: List[List[int]] = instances['M_list'][i]
        
        solution: List[int] = solve_instance(n, P, Q, k_list, m_list, T_list, M_list)
        solutions.append(solution)
    
    return solutions


def print_solutions(predicted: List[List[int]], actual: List[List[int]]):
    print("Test cases:")
    print("{:<40} {:<40} {:<10}".format("Predicted", "Actual", "Match?"))
    print("-" * 90)
    
    for predicted, actual in zip(predicted, actual):
        pred_str = str(predicted)
        actual_str = str(actual)
        match = "✓" if predicted == actual else "✗"
        print("{:<40} {:<40} {:<10}".format(pred_str[:37] + "..." if len(pred_str) > 40 else pred_str, 
                                            actual_str[:37] + "..." if len(actual_str) > 40 else actual_str, 
                                            match))
    
    print("\nOverall match:", "✓" if predicted == actual else "✗")

if __name__ == '__main__':
    with open('./tests/test_set_small_instances', 'rb') as f:
        small_instances = pickle.load(f)
    with open('./tests/test_set_medium_instances', 'rb') as f:
        medium_instances = pickle.load(f)
    with open('./tests/test_set_large_instances', 'rb') as f:
        large_instances = pickle.load(f)

    small_predicted = solve_all_instances(small_instances)
    medium_predicted = solve_all_instances(medium_instances)
    large_predicted = solve_all_instances(large_instances)

    pickle.dump(small_predicted, open('small_solutions', 'wb'))
    pickle.dump(medium_predicted, open('medium_solutions', 'wb'))
    pickle.dump(large_predicted, open('large_solutions', 'wb'))
