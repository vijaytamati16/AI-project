from sympy import symbols, Eq, solve, diff, integrate, sympify

def advanced_math_solver():
    print("Welcome to the Advanced Math Solver!")
    print("Options:")
    print("1. Solve Arithmetic (e.g., 5 + 3 * 2)")
    print("2. Solve Linear Equations (e.g., 2*x + 3 = 7)")
    print("3. Solve Multiple Variable Equations (e.g., 2*x + y = 5, x - y = 3)")
    print("4. Solve Polynomial Equations (e.g., x**2 - 4 = 0)")
    print("5. Compute Derivatives (e.g., derivative of 3*x**2 + 2*x)")
    print("6. Compute Integrals (e.g., integral of 3*x**2 + 2*x)")
    print("7. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-7): ")
        if choice == '1':
            try:
                expression = input("Enter an arithmetic expression: ")
                result = eval(expression)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            try:
                equation = input("Enter a linear equation (e.g., 2*x + 3 = 7): ")
                var = symbols('x')
                lhs, rhs = equation.split('=')
                eq = Eq(sympify(lhs.strip()), sympify(rhs.strip()))
                solution = solve(eq, var)
                print(f"Solution: x = {solution}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '3':
            try:
                num_eq = int(input("How many equations? "))
                equations = []
                variables = symbols(input("Enter variables separated by space (e.g., x y z): "))
                for i in range(num_eq):
                    eq = input(f"Enter equation {i + 1} (e.g., 2*x + y = 5): ")
                    lhs, rhs = eq.split('=')
                    equations.append(Eq(sympify(lhs.strip()), sympify(rhs.strip())))
                solution = solve(equations, variables)
                print(f"Solutions: {solution}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '4':
            try:
                polynomial = input("Enter a polynomial equation (e.g., x**2 - 4 = 0): ")
                var = symbols('x')
                lhs, rhs = polynomial.split('=')
                eq = Eq(sympify(lhs.strip()), sympify(rhs.strip()))
                solutions = solve(eq, var)
                print(f"Solutions: {solutions}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '5':
            try:
                expression = input("Enter a function (e.g., 3*x**2 + 2*x): ")
                variable = symbols(input("Enter the variable (e.g., x): "))
                derivative = diff(sympify(expression.strip()), variable)
                print(f"Derivative: {derivative}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '6':
            try:
                expression = input("Enter a function (e.g., 3*x**2 + 2*x): ")
                variable = symbols(input("Enter the variable (e.g., x): "))
                integral = integrate(sympify(expression.strip()), variable)
                print(f"Integral: {integral}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '7':
            print("Exiting Math Solver. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    advanced_math_solver()
