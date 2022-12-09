import json


def load_candidates(file):
    """ Load json file format in list"""
    with open(file, encoding="utf-8") as f:
        data_candidates = json.load(f)
    return data_candidates


def get_all(filename):
    """return all candidates: name: [pk, skills]"""
    candidates = dict()
    for i in range(len(filename)):
        candidates[filename[i]['pk']] = [filename[i]["name"], "".join(filename[i]["skills"]).lower()]
    return candidates


def get_by_pk(pk, data_candidates):
    """return name candidate of pk"""
    candidate = data_candidates[pk]
    url = f'{data_candidates[pk]["picture"]}'
    return candidate, str(url)


def get_by_skill(skill_name, candidates):
    """return names candidate of skills"""
    valid_candidates = str()
    for k, v in candidates.items():
        if skill_name in v[1]:
            valid_candidates += f"<pre>\n{v[0]} -\n{k}\n{v[1][0:]}\n<pre>\n"
    return valid_candidates
