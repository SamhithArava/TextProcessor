positive_words = [
    "good", "excellent", "amazing", "happy", "great"
]

negative_words = [
    "bad", "terrible", "worst", "poor", "boring", "difficult"
]

def analyze_chunk(chunk):
    positive_count = 0
    negative_count = 0

    for line in chunk:
        words = line.lower().split()

        i = 0
        while i < len(words):

            # Handle "not good"
            if i < len(words) - 1 and words[i] == "not":
                next_word = words[i+1]
                if next_word in positive_words:
                    negative_count += 1
                    i += 2
                    continue

            # Handle "very good"
            if i < len(words) - 1 and words[i] == "very":
                next_word = words[i+1]
                if next_word in positive_words:
                    positive_count += 2   # strong positive
                    i += 2
                    continue

            word = words[i]

            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
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