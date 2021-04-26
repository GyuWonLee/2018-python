rows = 3
cols = 5

i = 1
s = []
for row in range(rows):
    e = []
    for row in range(cols):
        e.append(i)
        i += 1
    s.append(e)
    
print("s=",s)

