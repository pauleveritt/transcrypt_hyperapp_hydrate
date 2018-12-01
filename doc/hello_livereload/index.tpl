<html>
<head>
    <title>Transcrypt Hyperapp</title>
    <link rel="icon" type="image/x-icon"
          href="https://www.python.org/static/favicon.ico">
    <link rel="stylesheet" href="index.css"/>
    <script src="hyperapp.js"></script>
    <script src="hyperappHtml.js"></script>
</head>
<body>
<h1>Transcrypt + Hyperapp Demo</h1>
<p>This sample application has a counter. On first load, the counter
    renders, server-side, the HTML. After that, client-side events
    re-render the counter.</p>
<div id="counter">
    <div>
        <h3>Counter Demo</h3>
        <p>Current Count: {{ state['count'] }}</p>
        <button>-</button>
        <button>+</button>
    </div>
</div>
<script src="counter.js"></script>
</body>
</html>
