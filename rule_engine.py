positive_rules = {
    "excellent": 3,
    "amazing": 2,
    "good": 1,
    "happy": 2
}

negative_rules = {
    "terrible": -3,
    "bad": -1,
    "worst": -2,
    "error": -2
}

def analyze_chunk(chunk):
    score = 0

    for line in chunk:
        words = line.lower().split()
        for word in words:
            if word in positive_rules:
                score += positive_rules[word]
            elif word in negative_rules:
                score += negative_rules[word]

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment