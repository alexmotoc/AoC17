class Particle:
    def __init__(self, p, v, a):
        self.p = [int(x) for x in p]
        self.v = [int(x) for x in v]
        self.a = [int(x) for x in a]

    def update_particle(self):
        """Returns the updated particle after performing a tick"""
        for i in xrange(3):
            # Increase velocity by accelaration
            self.v[i] += self.a[i]
            # Increase position by velocity
            self.p[i] += self.v[i]

    def same_position(self, particle):
        """Returns true if two particles occupy the same position"""
        same = True

        for i in xrange(3):
            if self.p[i] != particle.p[i]:
                same = False

        return same

    def __str__(self):
        """Returns a string representation of the particle"""
        position = ','.join([str(x) for x in self.p])
        velocity = ','.join([str(x) for x in self.v])
        acceleration = ','.join([str(x) for x in self.a])
        return 'p=<' + position + '> v=<' + velocity + '> a=<' + acceleration + '>'

def manhattan_distance(attribute):
    """Returns the Manhattan distance of the particle's attribute"""
    distance = 0

    for i in xrange(3):
        distance += abs(attribute[i])

    return distance

particles = []

with open('day20_input.txt') as file:
    for line in file:
        particle = line.split(', ')
        position = particle[0][3:particle[0].index('>')].split(',')
        accelaration = particle[1][3:particle[1].index('>')].split(',')
        velocity = particle[2][3:particle[2].index('>')].split(',')

        p = Particle(position, accelaration, velocity)
        particles.append(p)

simulations = 1000
particles_copy = particles[:]

# Part 1
# Get minimum acceleration
min_acceleration = min(particles, key=lambda x: manhattan_distance(x.a))

# Get particles with the same minimum acceleration
same_acceleration = {}
for i in xrange(len(particles)):
    if manhattan_distance(particles[i].a) == manhattan_distance(min_acceleration.a):
        same_acceleration[i] = particles[i]

# If there is only on particle -> print its index
# Else need to perform simulation as sorting by minimum velocity does not always work
if len(same_acceleration) == 1:
    for index in same_acceleration:
        print(index)
else:
    for i in xrange(simulations):
        for index in same_acceleration:
            same_acceleration[index].update_particle()
    min_distance = min(same_acceleration.keys(),
            key=lambda x: manhattan_distance(same_acceleration[x].p))
    print(min_distance)

# Part 2 - brute force solution (run simulation)
for i in xrange(simulations):
    collisions = set()
    for i in xrange(len(particles_copy) - 1):
        for j in range(i + 1, len(particles_copy)):
            if particles_copy[i].same_position(particles_copy[j]):
                collisions.add(i)
                collisions.add(j)
    for i in sorted(collisions, reverse=True):
        particles_copy.pop(i)
    for particle in particles_copy:
        particle.update_particle()

print(len(particles_copy))