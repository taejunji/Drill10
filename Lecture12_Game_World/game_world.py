world = [[],[],[]]

def add_object(o, depth = 0):
    world[depth].append(o) # 지정된 깊이의 레이어에 객체 추가

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('왜 존재하지도 않는 걸 지우라고????')