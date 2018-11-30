<html>
<head>
    <title>Hyperapp Transcrypt</title>
    <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
    <link rel="stylesheet" href="demo.css"/>
    <script src="hyperapp.js"></script>
</head>
<body>
<h1>HyperApp Demo</h1>
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
<script type="module">
    import * as demo from './__target__/demo.js';

</script>
</body>
</html>
