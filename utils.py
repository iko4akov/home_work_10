import json


def load_candidates(file="candidates.json"):
    """ Load json file format in list"""
    with open(file, encoding="utf-8") as f:
        file = json.load(f)
    return file


def get_all(filename=load_candidates()):
    """return names candidates"""
    candidates = []
    for i in range(len(filename)):
        candidates.append(filename[i]["name"])
    return candidates


def get_by_pk(pk, candidates=get_all()):
    """return name candidate of pk"""
    if 0 < pk <= len(candidates):
        candidate = candidates[pk-1]
        return candidate
    else:
        return "pk nothing"


def get_by_skill(skill_name, file=load_candidates()):
    """return names candidate of skills"""
    need_name = []
    for i in range(len(file)):
        skills_lower = file[i]["skills"].lower().split(", ")
        if skill_name in skills_lower:
            need_name.append(file[i]["name"])
        else:
            continue
    return ", ".join(need_name)

# filename = load_candidates()
# candidates = get_all(filename)
# # print(get_by_pk(4))
# print(get_by_skill("go"))
