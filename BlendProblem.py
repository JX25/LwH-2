from pulp import *

mock_products = ["oatmeal", "chicken", "eggs", "milk", "pecan pie", "pork and beans"]
mock_data = {
    "protein": {
        "oatmeal": 4,
        "chicken": 32,
        "eggs": 13,
        "milk": 8,
        "pecan pie": 4,
        "pork and beans": 14
    },
    "energy": {
        "oatmeal": 110,
        "chicken": 205,
        "eggs": 160,
        "milk": 160,
        "pecan pie": 420,
        "pork and beans": 260
    },
    "calcium": {
        "oatmeal": 2,
        "chicken": 12,
        "eggs": 54,
        "milk": 285,
        "pecan pie": 22,
        "pork and beans": 80
    },
    "price": {
        "oatmeal": 0.30,
        "chicken": 2.4,
        "eggs": 1.3,
        "milk": 0.90,
        "pecan pie": 2.00,
        "pork and beans": 1.9
    }
}
mock_constraints = [
    "energy;>=;2000",
    "protein;>=;55",
    "calcium;>=;800"
]


class BlendProblem:
    def __init__(self):
        self.data_dict = {
            "products": [],
            "data": {},
            "constraints": [],
        }

    def update_products(self, name, value):
        print(name, value)
        name = name.split(";")
        if name[0] not in self.data_dict["products"]:
            self.data_dict["products"].append(name[0])
        if name[1] not in self.data_dict["data"].keys():
            self.data_dict["data"][name[1]] = {}
        self.data_dict["data"][name[1]][name[0]] = float(value)

    def update_constrain(self, constrain):
        print(constrain)
        if constrain not in self.data_dict["constraints"]:
            self.data_dict["constraints"].append(constrain)

    def solve(self):
        DEBUG = False

        if DEBUG:
            self.data_dict = {
                "products": mock_products,
                "data": mock_data,
                "constraints": mock_constraints
            }
        # Minimalizacja kosztow
        problem = LpProblem("Blending problem", LpMinimize)

        # zmienne dotyczace problemu
        problem_vars = LpVariable.dicts("AmountOf", self.data_dict["products"], 0)

        # funkcja celu
        problem += lpSum(self.data_dict["data"]["price"][i] * problem_vars[i] for i in self.data_dict["products"])

        # wymagane zaleznosci
        for constrain in self.data_dict["constraints"]:
            constrain = constrain.split(";")
            sign = constrain[1]
            value = constrain[2]
            constrain = constrain[0]
            if sign == "<=":
                problem += lpSum(self.data_dict["data"][constrain][i] * problem_vars[i] for i in
                                 self.data_dict["products"]) <= float(value)
            elif sign == ">=":
                problem += lpSum(self.data_dict["data"][constrain][i] * problem_vars[i] for i in
                                 self.data_dict["products"]) >= float(value)
            elif sign == "=":
                problem += lpSum(self.data_dict["data"][constrain][i] * problem_vars[i] for i in
                                 self.data_dict["products"]) == float(value)
            elif sign == ">":
                problem += lpSum(self.data_dict["data"][constrain][i] * problem_vars[i] for i in
                                 self.data_dict["products"]) > float(value)
            elif sign == "<":
                problem += lpSum(self.data_dict["data"][constrain][i] * problem_vars[i] for i in
                                 self.data_dict["products"]) < float(value)

        LpSolverDefault.msg = 1
        problem.solve()
        result = "Status: " + LpStatus[problem.status] +"\n"

        for i in problem.variables():
            result += i.name[9:] + " = " + str(i.varValue) + "\n"

        result += "Total cost: " + str(round(problem.objective.value(), 2))
        return result

