from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
<html>
<head>
<title> home page </title>
</head>
<body>
<h1>Hello,world</h1>
</body>
</html> '''

