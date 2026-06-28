import sympy as sp

# ponytail: minimal Newton-Raphson implementation returning list of dicts
def newton_raphson(func_str, dfunc_str, x0, tol=1e-5, max_iter=100):
    x = sp.Symbol('x')
    f = sp.lambdify(x, sp.sympify(func_str), 'math')
    df = sp.lambdify(x, sp.sympify(dfunc_str), 'math')
    
    history = []
    xn = x0
    for n in range(1, max_iter + 1):
        fxn = f(xn)
        dfxn = df(xn)
        if dfxn == 0:
            raise ZeroDivisionError("Turunan bernilai 0.")
            
        xn_next = xn - (fxn / dfxn)
        err = abs(xn_next - xn)
        
        history.append({
            "Iter": n, "x_n": round(xn, 6), "f(x_n)": round(fxn, 6),
            "f'(x_n)": round(dfxn, 6), "x_n+1": round(xn_next, 6), "Error": round(err, 6)
        })
        
        if err < tol:
            break
        xn = xn_next
        
    return history
