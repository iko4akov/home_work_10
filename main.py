from flask import Flask
from utils import load_candidates, get_all, get_by_skill, get_by_pk


filename = "candidates.json"

candidates = load_candidates(filename)

app = Flask(__name__)


@app.route("/")
def page_home(file=candidates):
    for candidate in file:
        return f"{candidate}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=0)


