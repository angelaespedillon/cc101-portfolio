lab = float(input(" Laboratory grade : "))
lecture = float(input("Lecture grade : "))
rating = lab * 0.65 + lecture * 0.35
print(f"Midterm rating: {rating:.2f}")