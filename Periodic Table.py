n = int(input())
chemical_compounds = set()

for _ in range(n):
    compounds = input().split()
    chemical_compounds = chemical_compounds.union(compounds)

print('\n'.join(chemical_compounds))
