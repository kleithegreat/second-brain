import pickle

def solve_instance(n, P, Q, k_list, m_list, T_list, M_list):
    solution = [False] * n
    changed = True
    
    while changed:
        changed = False
        
        # Check lead-to conditions
        for i in range(P):
            left_side = all(solution[T_list[i][j]] for j in range(k_list[i]))
            right_side = solution[T_list[i][-1]]
            
            if left_side and not right_side:
                solution[T_list[i][-1]] = True
                changed = True
        
        # Check False-must-exist conditions
        for i in range(Q):
            if all(solution[j] for j in M_list[i]):
                for j in M_list[i]:
                    if not solution[j]:
                        solution[j] = False
                        changed = True
                        break
    
    for i in range(P):
        left_side = all(solution[T_list[i][j]] for j in range(k_list[i]))
        right_side = solution[T_list[i][-1]]
        if left_side and not right_side:
            return []
    
    for i in range(Q):
        if all(solution[j] for j in M_list[i]):
            return []
    
    return [int(x) for x in solution]


def solve_all_instances(instances):
    solutions = []
    for i in range(instances['numInstances']):
        n = instances['n_list'][i]
        P = instances['P_list'][i]
        Q = instances['Q_list'][i]
        k_list = instances['k_list'][i]
        m_list = instances['m_list'][i]
        T_list = instances['T_list'][i]
        M_list = instances['M_list'][i]
        
        solution = solve_instance(n, P, Q, k_list, m_list, T_list, M_list)
        solutions.append(solution)
    
    return solutions


with open('./tests/examples_of_small_instances', 'rb') as f:
    small_instances = pickle.load(f)

with open('./tests/examples_of_medium_instances', 'rb') as f:
    medium_instances = pickle.load(f)

with open('./tests/examples_of_large_instances', 'rb') as f:
    large_instances = pickle.load(f)

small_solutions = solve_all_instances(small_instances)
medium_solutions = solve_all_instances(medium_instances)
large_solutions = solve_all_instances(large_instances)

# # Save solutions
# with open('small_solutions', 'wb') as f:
#     pickle.dump(small_solutions, f)
# 
# with open('medium_solutions', 'wb') as f:
#     pickle.dump(medium_solutions, f)
# 
# with open('large_solutions', 'wb') as f:
#     pickle.dump(large_solutions, f)
# 
# print("All instances solved and solutions saved.")


# with open('./tests/examples_of_instances', 'rb') as f:
#     instances = pickle.load(f)
# 
# with open('./tests/examples_of_solutions', 'rb') as f:
#     solutions = pickle.load(f)
# 
# print(f"Predicted: {solve_all_instances(instances)}")
# print(f"Expected: {solutions}")
# print(f"Match: {solve_all_instances(instances) == solutions}")
