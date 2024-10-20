s1 = {1, 2, 5, 8, 92}

s2 = {2, 8, 6, 94, 23}

print(s1.union(s2))
print(s1.intersection(s2))

print(f'Length of S1: {len(s1)}, and S2: {len(s2)}')
print(f'Union length: {len(s1.union(s2))}')
print(f'Intersection length: {len(s1.intersection(s2))}')

print(s1.difference(s2))

# isSubset - below values must be present in the Set s1
print({1,8}.issubset(s1))

# isSuperSet - is S1 superset for the asked set.
print(s1.issuperset({1,2}))

