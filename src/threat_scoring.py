def score_threat(data):
    score = 0
    if data.get("malicious"):
        score += 50
    if data.get("phishing"):
        score += 30
    return score