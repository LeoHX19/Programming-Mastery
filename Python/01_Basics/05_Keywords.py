import keyword

print("Python Keywords:\n")

for kw in keyword.kwlist:
    print(kw)

print("\nTotal Keywords:", len(keyword.kwlist))