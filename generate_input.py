feedbacks = [
    "The faculty teaching was excellent and very helpful",
    "The course content was good but could be improved",
    "The lab sessions were amazing and interactive",
    "The experience was bad due to lack of resources",
    "The teacher explained concepts clearly and nicely",
    "The class was boring and not engaging",
    "The project guidance was excellent and very useful",
    "The overall experience was terrible and stressful",
    "The course was good and well structured",
    "The teaching quality was poor and confusing",
    "very good teaching and excellent explanation",
    "not good teaching method",
    "good good bad explanation",
    "very bad experience in lab",
    "amazing support from faculty"
]

def generate_reviews(n):
    with open("student_feedback.csv", "w") as f:
        f.write("text\n")
        for i in range(n):
            f.write(feedbacks[i % len(feedbacks)] + "\n")


if __name__ == "__main__":
    generate_reviews(50000)