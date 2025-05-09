import mysql.connector
import pandas as pd

# MySQL DB connection setup
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ani@2004",
    database="employee_db"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        productivity INT,
        quality INT,
        teamwork INT,
        attendance INT,
        score FLOAT,
        category VARCHAR(50)
    )
""")

def evaluate_employee():
    name = input("Name: ")
    productivity = int(input("Productivity (0-10): "))
    while(True):
        if productivity>=0 and productivity<=10:
            break
        else:
            productivity = int(input("Productivity (0-10): "))
        
    quality = int(input("Quality of Work (0-10): "))
    while(True):
        if quality>=0 and quality<=10:
            break
        else:
            quality = int(input("quality (0-10): "))
    teamwork = int(input("Teamwork (0-10): "))
    while(True):
        if teamwork>=0 and teamwork<=10:
            break
        else:
            teamwork = int(input("teamwork (0-10): "))
    attendance = int(input("Attendance (0-10): "))
    while(True):
        if attendance>=0 and attendance<=10:
            break
        else:
            attendance = int(input("attendance (0-10): "))

    weights = {"Productivity": 0.3, "Quality": 0.3, "Teamwork": 0.2, "Attendance": 0.2}
    score = (
        productivity * weights["Productivity"] +
        quality * weights["Quality"] +
        teamwork * weights["Teamwork"] +
        attendance * weights["Attendance"]
    )

    if score >= 8:
        category = "Excellent"
    elif score >= 6:
        category = "Good"
    elif score >= 4:
        category = "Average"
    else:
        category = "Needs Improvement"

    cursor.execute("""
        INSERT INTO evaluations (name, productivity, quality, teamwork, attendance, score, category)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (name, productivity, quality, teamwork, attendance, score, category))
    conn.commit()
    print(f"✅ {name} evaluated! Score: {round(score, 2)} / 10, Category: {category}")

def show_all_evaluations():
    cursor.execute("SELECT * FROM evaluations")
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['ID', 'Name', 'Productivity', 'Quality', 'Teamwork', 'Attendance', 'Score', 'Category'])
    print("\nAll Evaluations:\n", df)

def main():
    while True:
        print("\n1. Evaluate Employee")
        print("2. Show All Evaluations")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        if choice == '1':
            evaluate_employee()
        elif choice == '2':
            show_all_evaluations()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    try:
        main()
    finally:
        cursor.close()
        conn.close()