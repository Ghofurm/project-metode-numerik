import sympy as sp

# ponytail: minimal Iterasi Sederhana implementation returning list of dicts
def iterasi(g_str, x0, tol=1e-5, max_iter=100):
    x = sp.Symbol('x')
    g = sp.lambdify(x, sp.sympify(g_str), 'math')
    
    history = []
    xn = x0
    for n in range(1, max_iter + 1):
        xn_next = g(xn)
        err = abs(xn_next - xn)
        
        history.append({
            "Iter": n, "x_n": round(xn, 6), "x_n+1": round(xn_next, 6), "Error": round(err, 6)
        })
        
        if err < tol:
            break
        xn = xn_next
        
    return history
