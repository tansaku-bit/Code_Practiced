with open('set.txt', 'w') as f:
    for i in range(0, 1000000000, 100000):
        start = i + 1
        end = i + 100000
        f.write(f"[{start}, {end}]\n")
