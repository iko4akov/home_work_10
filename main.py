from flask import Flask
from utils import load_candidates, get_all, get_by_skill, get_by_pk


adress_file = "candidates.json"


data_candidates = load_candidates(adress_file)


candidates = get_all(data_candidates)


app = Flask(__name__)


@app.route("/")
def page_home():
    home = str()
    for k, v in candidates.items():
        home += f"<pre>\n{v[0]} -\n{k}\n{v[1][0:]}\n</pre>\n"
    return f"{home}"


@app.route("/candidates/<int:pk>")
def page_candidates(pk):
    candidate, url = get_by_pk(pk, data_candidates)
    return f"<img src='{url}'>\n<pre>\n{candidate['name']}\n{pk}\n{candidate['skills']}\n</pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    return get_by_skill(skill, candidates)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5)


