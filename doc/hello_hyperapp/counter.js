const {app} = window.hyperapp;
const html = window.hyperappHtml;
const {h3, p, div, button} = html;

const state = {
  count: 0
}

const actions = {
  down: () => state => ({ count: state.count - 1 }),
  up: () => state => ({ count: state.count + 1 })
}

const view = (state, actions) =>
  div([
    h3('Counter Demo'),
    p('Current Count: ' + state.count),
    button({ onclick: actions.down }, "-"),
    button({ onclick: actions.up }, "+")
  ])

app(state, actions, view, document.getElementById("counter"))
