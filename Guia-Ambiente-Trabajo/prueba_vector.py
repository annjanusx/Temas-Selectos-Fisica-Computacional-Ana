import vector

p = vector.obj(
    px=30.0,
    py=40.0,
    pz=100.0,
    E=120.0,
)

print("pT =", p.pt)
print("|p| =", p.p)
print("masa invariante =", p.mass)