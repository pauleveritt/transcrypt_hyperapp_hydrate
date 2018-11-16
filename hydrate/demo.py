hyperapp = window.hyperapp
h = window.hyperapp.h
app = window.hyperapp.app

state = dict(count=0)

actions = dict(
    down=lambda value: lambda s: dict(count=s.count - value),
    up=lambda value: lambda s: dict(count=s.count + value),
)

view = lambda s, a: h(
    'div', {}, [
        h("h1", {}, s.count),
        h("button", dict(onclick=lambda: a.down(1)), "-"),
        h("button", dict(onclick=lambda: a.up(1)), "+")
    ]
)

target = document.getElementById("output")
app(state, actions, view, target)
