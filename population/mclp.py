import pandas as pd
from pulp import LpProblem, LpVariable, lpSum, LpMinimize

# CSV 파일에서 데이터 읽기
def read_csv(file_path):
    return pd.read_csv(file_path)

# MCLP 문제 해결 함수
def solve_mclp(customers, facilities, coverage_matrix, opening_cost, budget):
    model = LpProblem("MCLP", LpMinimize)

    # Binary variables indicating whether to open a facility
    x = LpVariable.dicts("open", facilities, cat="Binary")

    # Binary variables indicating whether a customer is covered
    y = LpVariable.dicts("cover", customers, cat="Binary")

    # Objective function: minimize total cost
    model += lpSum(opening_cost[facility] * x[facility] for facility in facilities)

    # Constraints: budget constraint
    model += lpSum(opening_cost[facility] * x[facility] for facility in facilities) <= budget

    # Constraints: coverage constraints
    for customer in customers:
        model += lpSum(coverage_matrix[customer][facility] * x[facility] for facility in facilities) >= y[customer]

    # Solve the problem
    model.solve()

    # Display the results
    print("Status:", model.status)
    print("Objective Value:", model.objective.value())
    selected_facilities = [facility for facility in facilities if x[facility].value() == 1]
    print("Selected Facilities:", selected_facilities)

# 예시 데이터 로드
customers = read_csv("customers.csv")
facilities = read_csv("facilities.csv")
coverage_matrix = read_csv("coverage_matrix.csv")
opening_cost = dict(zip(facilities["FacilityID"], facilities["OpeningCost"]))
budget = 100000  # 예시로 설정한 예산

# MCLP 문제 해결
solve_mclp(customers["CustomerID"], facilities["FacilityID"], coverage_matrix, opening_cost, budget)
