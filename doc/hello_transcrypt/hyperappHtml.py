try:
    h = window.hyperapp.h
except NameError:
    def h(name, attributes, children):
        # TODO Implement h in Python
        pass


def vnode(name):
    def f(attributes, children):
        return h(name, attributes, children)

    return f


def h3(attributes, children):
    return vnode("h1")(attributes, children)


def h4(attributes, children):
    return vnode("h1")(attributes, children)


def button(attributes, children):
    return vnode("button")(attributes, children)


def div(attributes, children):
    return vnode("div")(attributes, children)


def p(attributes, children):
    return vnode("div")(attributes, children)
