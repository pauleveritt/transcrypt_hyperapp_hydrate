from hydrate.html import button, div, h3, p

state = dict(count=11)

actions = dict(
    down=lambda value: lambda s: dict(count=s.count - value),
    up=lambda value: lambda s: dict(count=s.count + value),
)


def view(st, ac):
    return div({}, [
        h3({}, 'Welcome Counter'),
        p({}, 'Current Counter: ' + str(st.count)),
        button(dict(onclick=lambda: ac.down(1)), "-"),
        button(dict(onclick=lambda: ac.up(1)), "+")
    ])


try:
    window.hyperapp.app(
        state,
        actions,
        view,
        document.getElementById("counter")
    )
except NameError:
    pass
