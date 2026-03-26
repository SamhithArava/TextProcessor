import random

feedbacks = [
    "The teaching was excellent and very helpful",
    "The course content was good",
    "The class was amazing and interactive",
    "The experience was bad and boring",
    "The teacher explanation was poor",
    "The session was difficult to understand",
    "good good bad explanation",
    "not good teaching method",
    "very good teaching and excellent explanation",
    "terrible experience in lab",
    "average experience nothing special",
    "it is okay not bad not great"
]

def generate_reviews(n):
    with open("student_feedback.csv", "w") as f:
        f.write("text\n")
        for i in range(n):
            f.write(random.choice(feedbacks) + "\n")

if __name__ == "__main__":
    generate_reviews(50000)