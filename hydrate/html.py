def python_h(name, attributes, children):
    x = '''
export function h(name, attributes) {
  var rest = []
  var children = []
  var length = arguments.length

  while (length-- > 2) rest.push(arguments[length])

  while (rest.length) {
    var node = rest.pop()
    if (node && node.pop) {
      for (length = node.length; length--; ) {
        rest.push(node[length])
      }
    } else if (node != null && node !== true && node !== false) {
      children.push(node)
    }
  }

  return typeof name === "function"
    ? name(attributes || {}, children)
    : {
        nodeName: name,
        attributes: attributes || {},
        children: children,
        key: attributes && attributes.key
      }
}    
    '''
    pass


try:
    h = window.hyperapp.h
except NameError:
    def h():
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
