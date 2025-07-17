import sqlite3
import pandas as pd

# Create a connection to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('example.db')

# Sample data
students_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'age': [20, 21, 19, 22, 20],
    'grade': ['A', 'B', 'A', 'C', 'B']
}

courses_data = {
    'course_id': [101, 102, 103],
    'course_name': ['Math', 'Physics', 'Chemistry'],
    'credits': [3, 4, 3]
}

# Create DataFrames
students_df = pd.DataFrame(students_data)
courses_df = pd.DataFrame(courses_data)

print("Original DataFrames:")
print("\nStudents:")
print(students_df)
print("\nCourses:")
print(courses_df)

# 1. Write DataFrames to SQLite database
students_df.to_sql('students', conn, if_exists='replace', index=False)
courses_df.to_sql('courses', conn, if_exists='replace', index=False)

print("\n" + "="*50)
print("Data written to SQLite database successfully!")

# 2. Read data back from SQLite using pandas
print("\n" + "="*50)
print("Reading data from SQLite:")

# Read entire table
students_from_db = pd.read_sql_query("SELECT * FROM students", conn)
print("\nAll students from database:")
print(students_from_db)

# 3. SQL queries with pandas
print("\n" + "="*50)
print("SQL Queries:")

# Query with WHERE clause
young_students = pd.read_sql_query(
    "SELECT name, age FROM students WHERE age < 21", 
    conn
)
print("\nStudents younger than 21:")
print(young_students)

# Query with ORDER BY
top_students = pd.read_sql_query(
    "SELECT name, grade FROM students WHERE grade IN ('A', 'B') ORDER BY grade", 
    conn
)
print("\nTop students (A and B grades):")
print(top_students)

# 4. More complex operations
print("\n" + "="*50)
print("Advanced Operations:")

# Add new student using pandas
new_student = pd.DataFrame({
    'id': [6],
    'name': ['Frank'],
    'age': [23],
    'grade': ['A']
})

# Append to existing table
new_student.to_sql('students', conn, if_exists='append', index=False)

# Verify addition
all_students = pd.read_sql_query("SELECT * FROM students ORDER BY id", conn)
print("\nAfter adding new student:")
print(all_students)

# 5. Aggregation queries
print("\n" + "="*50)
print("Aggregation Examples:")

# Count students by grade
grade_counts = pd.read_sql_query(
    "SELECT grade, COUNT(*) as count FROM students GROUP BY grade ORDER BY grade", 
    conn
)
print("\nStudents count by grade:")
print(grade_counts)

# Average age
avg_age = pd.read_sql_query("SELECT AVG(age) as average_age FROM students", conn)
print(f"\nAverage age: {avg_age['average_age'][0]:.1f}")

# 6. Update data
print("\n" + "="*50)
print("Update Operations:")

# Update using raw SQL
cursor = conn.cursor()
cursor.execute("UPDATE students SET grade = 'A+' WHERE name = 'Alice'")
conn.commit()

# Read updated data
updated_students = pd.read_sql_query("SELECT * FROM students WHERE name = 'Alice'", conn)
print("\nAfter updating Alice's grade:")
print(updated_students)

# 7. Working with dates
print("\n" + "="*50)
print("Working with Dates:")

# Create enrollment data with dates
enrollment_data = {
    'student_id': [1, 2, 3, 4, 5],
    'enrollment_date': pd.date_range('2024-01-15', periods=5, freq='D')
}

enrollment_df = pd.DataFrame(enrollment_data)
enrollment_df.to_sql('enrollment', conn, if_exists='replace', index=False)

# Query with date filtering
recent_enrollments = pd.read_sql_query(
    "SELECT * FROM enrollment WHERE enrollment_date >= '2024-01-17'", 
    conn
)
print("\nEnrollments from 2024-01-17 onwards:")
print(recent_enrollments)

# 8. JOIN operations
print("\n" + "="*50)
print("JOIN Operations:")

# First, let's create a simple relationship
enrollments_simple = pd.DataFrame({
    'student_id': [1, 2, 3, 1, 2],
    'course_id': [101, 102, 101, 103, 101]
})
enrollments_simple.to_sql('enrollments', conn, if_exists='replace', index=False)

# JOIN query
join_result = pd.read_sql_query("""
    SELECT s.name, c.course_name 
    FROM students s 
    JOIN enrollments e ON s.id = e.student_id 
    JOIN courses c ON e.course_id = c.course_id
    ORDER BY s.name, c.course_name
""", conn)
print("\nStudent-Course enrollments:")
print(join_result)

# 9. List all tables in the database
print("\n" + "="*50)
print("Database Schema:")

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'", 
    conn
)
print("\nTables in database:")
print(tables)

# 10. Clean up
print("\n" + "="*50)
print("Cleanup:")

# Close connection
conn.close()
print("Database connection closed.")

# Note: The database file 'example.db' will remain in your directory
# You can delete it manually if needed

print("\n" + "="*50)
print("Key takeaways:")
print("• Use pd.to_sql() to write DataFrames to SQLite")
print("• Use pd.read_sql_query() to read data with SQL queries")
print("• SQLite is great for local development and small applications")
print("• Always close your database connections")
print("• You can use complex SQL queries with pandas for powerful data analysis")