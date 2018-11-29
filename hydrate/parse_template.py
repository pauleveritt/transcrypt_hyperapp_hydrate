from jinja2 import Environment


def parsed():
    env = Environment(loader=None)
    p = env.parse('<h1><p>{{ state.count + 1 }}</p></h1>')
    output = p.body[0]
    nodes = output.nodes
    for node in nodes:
        print(node)


if __name__ == '__main__':
    parsed()
