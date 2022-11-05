def cipher(X):
    ans = ""
    for i in range(len(X)):
        if 'a' <= X[i] <= 'z':
            ans += chr(219 - ord(X[i]))
        
        else:
            ans += X[i]

    return ans

x = 'Tomato'
X = cipher(x)
print(X)
X_ = cipher(X)
print(X_)
