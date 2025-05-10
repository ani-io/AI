def evaluate_performance():
    print("Welcome to EMP-EVAL Expert System")
    print("Please answer the following with yes or no:\n")

    punctual = input("Is the employee punctual? ").lower()
    tasks_on_time = input("Does the employee complete tasks on time? ").lower()
    quality_work = input("Does the employee produce quality work? ").lower()
    teamwork = input("Is the employee good at teamwork? ").lower()
    initiative = input("Does the employee take initiative? ").lower()
    learning = input("Is the employee willing to learn new things? ").lower()

    score = 0

    # Each good response adds to the performance score
    if punctual == "yes":
        score += 1
    if tasks_on_time == "yes":
        score += 1
    if quality_work == "yes":
        score += 1
    if teamwork == "yes":
        score += 1
    if initiative == "yes":
        score += 1
    if learning == "yes":
        score += 1

    print("\n--- Performance Evaluation Result ---")

    if score == 6:
        print("Excellent Performance ⭐⭐⭐⭐⭐")
    elif score >= 4:
        print("Good Performance ⭐⭐⭐⭐")
    elif score >= 2:
        print("Average Performance ⭐⭐⭐")
    else:
        print("Needs Improvement ⭐")

    print("\nThank you for using EMP-EVAL!")

# Run the expert system
evaluate_performance()
