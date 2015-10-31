
generators = [(val for dummy in [0])
              for val in [1]]
val = 99
print(next(generators[0]))  # => py2: 99, py3: 1


generators = [(lambda val: (val for dummy in [0]))(val)
              for val in [1]]
val = 99
print(next(generators[0]))  # => 1


generators = []
for val in [1]:
    generators.append((val for dummy in [0]))

val = 99
print(next(generators[0]))  # => 99


generators = []
for val in [1]:
    generators.append((lambda val: (val for dummy in [0]))(val))

val = 99
print(next(generators[0]))  # => 1
