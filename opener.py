import subprocess

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/open/<path:path>')
def open(path):
    if not path.startswith("/"):
        path = "/" + path
    line_number = request.args.get("line-number", "1")
    subprocess.run(["open-file", path, line_number])
    return f"{path} {line_number}"
