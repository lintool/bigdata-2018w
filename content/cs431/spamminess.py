def spamminess(f: list, w: dict):
    """compute spamminess of feature list f using weights w""" 
    score = 0
    for feature in f:
        score += w.get(feature,0)
    return score
