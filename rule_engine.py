positive_words = ["good", "excellent", "happy", "great", "amazing"]
negative_words = ["bad", "terrible", "sad", "worst", "poor"]

def analyze_chunk(chunk):
    positive_count = 0
    negative_count = 0

    for line in chunk:
        words = line.lower().split()
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1

    score = positive_count - negative_count

    if score > 0:
        tag = "Positive"
    elif score < 0:
        tag = "Negative"
    else:
        tag = "Neutral"

    return score, tag