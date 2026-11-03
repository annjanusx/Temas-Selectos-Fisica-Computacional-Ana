from particle import Particle

electron = Particle.from_pdgid(11)
muon = Particle.from_pdgid(13)
top = Particle.from_pdgid(6)

print(electron)
print(muon)
print(top)