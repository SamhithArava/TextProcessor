def generate_reviews(n):
    with open("input.txt", "w") as f:
        for i in range(n):
            f.write("This product is amazing but has one minor error\n")


if __name__ == "__main__":
    n = int(input("Enter number of reviews to generate: "))
    generate_reviews(n)
    print(f"{n} reviews generated successfully.")