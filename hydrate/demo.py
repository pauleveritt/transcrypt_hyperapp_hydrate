from hydrate.html import button, div, h3, h4

state = dict(count=11)

actions = dict(
    down=lambda value: lambda s: dict(count=s.count - value),
    up=lambda value: lambda s: dict(count=s.count + value),
)


def view(st, ac):
    return div({}, [
        h3({}, 'Welcome Counter'),
        h4({}, st.count),
        [h3({}, i) for i in ('Hello!', 'Goodbye')],
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
