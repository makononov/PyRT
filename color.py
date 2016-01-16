BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
EAGLES_GREEN = (0, 29, 33)

def scale(color, factor):
    return list([max(min(int(x * factor), 255), 0) for x in color])

def component_scale(color, factors):
    return list([max(min(int(x * y), 255), 0) for x,y in zip(color, factors)])

def add(first, second):
    return list([max(min(int(x + y), 255), 0) for x,y in zip(first, second)])
