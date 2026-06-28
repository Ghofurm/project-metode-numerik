import sympy as sp

# ponytail: minimal Regula-Falsi implementation returning list of dicts
def regula_falsi(func_str, a, b, tol=1e-5, max_iter=100):
    x = sp.Symbol('x')
    f = sp.lambdify(x, sp.sympify(func_str), 'math')
    
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda.")
        
    history = []
    for n in range(1, max_iter + 1):
        c = b - (fb * (b - a)) / (fb - fa)
        fc = f(c)
        err = abs(b - a) # ponytail: simple error estimate
        
        history.append({
            "Iter": n, "a": round(a, 6), "b": round(b, 6), 
            "c": round(c, 6), "f(c)": round(fc, 6), "Error": round(err, 6)
        })
        
        if abs(fc) < tol or err < tol:
            break
            
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
            
    return history
