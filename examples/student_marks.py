"""Calculate a student's average and pass/fail result."""

marks = []

for subject_number in range(1, 4):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject_number} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a number.")

average = sum(marks) / len(marks)
print(f"Average: {average:.2f}")
print("Result:", "Pass" if average >= 50 else "Needs improvement")
