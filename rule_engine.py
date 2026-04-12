positive_words = {"good", "excellent", "amazing", "happy", "great"}
negative_words = {"bad", "terrible", "worst", "poor", "boring", "difficult"}

def analyze_text(text):
    words = text.lower().split()

    positive_count = 0
    negative_count = 0

    i = 0
    while i < len(words):

        # not good → negative
        if i < len(words)-1 and words[i] == "not":
            if words[i+1] in positive_words:
                negative_count += 1
                i += 2
                continue

        # very good → strong positive
        if i < len(words)-1 and words[i] == "very":
            if words[i+1] in positive_words:
                positive_count += 2
                i += 2
                continue

        if words[i] in positive_words:
            positive_count += 1
        elif words[i] in negative_words:
            negative_count += 1

        i += 1

    score = positive_count - negative_count

    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return score, sentiment