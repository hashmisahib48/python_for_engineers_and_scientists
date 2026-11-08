# Problem 5.4  Edges, boundary and neighbors of a triangle mesh
nx, ny = 4, 3                      # squares along x and y
# node number of the grid point in column i and row j
num = [[j * (nx + 1) + i for j in range(ny + 1)]
       for i in range(nx + 1)]
tris = []
for i in range(nx):
    for j in range(ny):
        a, b = num[i][j], num[i + 1][j]
        c, d = num[i + 1][j + 1], num[i][j + 1]
        tris += [(a, b, c), (a, c, d)]   # split along a-c
n_nodes = (nx + 1) * (ny + 1)

count = {}                         # edge -> number of triangles
for t in tris:
    for p, q in [(t[0], t[1]), (t[1], t[2]), (t[2], t[0])]:
        edge = (min(p, q), max(p, q))
        count[edge] = count.get(edge, 0) + 1
edges = set(count)
boundary = {e for e in edges if count[e] == 1}
b_nodes = {n for e in boundary for n in e}

neighbors = {n: set() for n in range(n_nodes)}
for p, q in edges:
    neighbors[p].add(q)
    neighbors[q].add(p)
degree = [len(neighbors[n]) for n in range(n_nodes)]

v, e, f = n_nodes, len(edges), len(tris)
print(f'V = {v}, E = {e}, F = {f}, V - E + F = {v - e + f}')
print(f'Boundary edges: {len(boundary)}, '
      f'perimeter edges expected: {2 * (nx + ny)}')
print(f'Interior nodes: {sorted(set(range(v)) - b_nodes)}')
print(f'Neighbors of node 6: {sorted(neighbors[6])}')
print(f'Degree: min {min(degree)}, max {max(degree)}, '
      f'mean {sum(degree) / v:.3f} = 2E/V')
