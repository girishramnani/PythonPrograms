w = lambda f : lambda n : 1 if n==1 else n*f(f)(n-1)
w2 = w(w)
print(w2(5))