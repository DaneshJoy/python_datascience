import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import numpy as np
from datetime import datetime, timedelta

# Database connection parameters
# Replace these with your actual PostgreSQL credentials
DB_CONFIG = {
    'host': 'localhost',
    'database': 'education_db',
    'user': 'your_username',
    'password': 'your_password',
    'port': 5432
}

# Create SQLAlchemy engine (recommended for pandas integration)
engine = create_engine(
    f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# Alternative: Direct psycopg2 connection
def create_psycopg2_connection():
    return psycopg2.connect(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        port=DB_CONFIG['port']
    )

print("PostgreSQL with Pandas - Educational Example")
print("=" * 60)

# Sample data
students_data = {
    'student_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'Diana Prince', 'Eve Adams', 'Frank Miller'],
    'age': [20, 21, 19, 22, 20, 23],
    'grade': ['A', 'B', 'A', 'C', 'B', 'A'],
    'enrollment_date': pd.date_range('2024-01-15', periods=6, freq='D'),
    'gpa': [3.8, 3.2, 3.9, 2.8, 3.4, 3.7],
    'is_active': [True, True, False, True, True, True]
}

courses_data = {
    'course_id': [101, 102, 103, 104, 105],
    'course_name': ['Advanced Mathematics', 'Quantum Physics', 'Organic Chemistry', 'Computer Science', 'Literature'],
    'credits': [4, 4, 3, 3, 2],
    'instructor': ['Dr. Smith', 'Prof. Johnson', 'Dr. Williams', 'Prof. Davis', 'Dr. Brown'],
    'max_students': [30, 25, 35, 40, 20]
}

departments_data = {
    'dept_id': [1, 2, 3, 4],
    'dept_name': ['Mathematics', 'Physics', 'Chemistry', 'Computer Science'],
    'budget': [150000, 200000, 175000, 300000],
    'established': pd.to_datetime(['1950-01-01', '1955-01-01', '1960-01-01', '1970-01-01'])
}

try:
    # 1. Create DataFrames
    students_df = pd.DataFrame(students_data)
    courses_df = pd.DataFrame(courses_data)
    departments_df = pd.DataFrame(departments_data)
    
    print("Original DataFrames:")
    print("\nStudents:")
    print(students_df)
    print("\nCourses:")
    print(courses_df)
    print("\nDepartments:")
    print(departments_df)
    
    # 2. Write DataFrames to PostgreSQL
    print("\n" + "="*60)
    print("Writing data to PostgreSQL...")
    
    # Using SQLAlchemy engine (recommended)
    students_df.to_sql('students', engine, if_exists='replace', index=False, method='multi')
    courses_df.to_sql('courses', engine, if_exists='replace', index=False, method='multi')
    departments_df.to_sql('departments', engine, if_exists='replace', index=False, method='multi')
    
    print("Data written successfully!")
    
    # 3. Read data back from PostgreSQL
    print("\n" + "="*60)
    print("Reading data from PostgreSQL:")
    
    # Read entire table
    students_from_db = pd.read_sql_query("SELECT * FROM students ORDER BY student_id", engine)
    print("\nAll students from database:")
    print(students_from_db)
    
    # 4. Basic SQL queries
    print("\n" + "="*60)
    print("Basic SQL Queries:")
    
    # Query with WHERE and ORDER BY
    high_gpa_students = pd.read_sql_query("""
        SELECT name, gpa, grade 
        FROM students 
        WHERE gpa >= 3.5 
        ORDER BY gpa DESC
    """, engine)
    print("\nStudents with GPA >= 3.5:")
    print(high_gpa_students)
    
    # Query with date filtering
    recent_enrollments = pd.read_sql_query("""
        SELECT name, enrollment_date, age 
        FROM students 
        WHERE enrollment_date >= '2024-01-17'
        ORDER BY enrollment_date
    """, engine)
    print("\nStudents enrolled from 2024-01-17 onwards:")
    print(recent_enrollments)
    
    # 5. Advanced PostgreSQL features
    print("\n" + "="*60)
    print("Advanced PostgreSQL Features:")
    
    # Array operations (if you have array columns)
    # JSON operations
    # Window functions
    advanced_query = pd.read_sql_query("""
        SELECT 
            name,
            age,
            gpa,
            RANK() OVER (ORDER BY gpa DESC) as gpa_rank,
            CASE 
                WHEN gpa >= 3.7 THEN 'Excellent'
                WHEN gpa >= 3.3 THEN 'Good'
                WHEN gpa >= 3.0 THEN 'Average'
                ELSE 'Below Average'
            END as performance_category
        FROM students
        WHERE is_active = true
        ORDER BY gpa DESC
    """, engine)
    print("\nStudent rankings with performance categories:")
    print(advanced_query)
    
    # 6. Aggregation and grouping
    print("\n" + "="*60)
    print("Aggregation Examples:")
    
    # Group by and aggregate
    grade_stats = pd.read_sql_query("""
        SELECT 
            grade,
            COUNT(*) as student_count,
            AVG(gpa) as avg_gpa,
            MIN(age) as min_age,
            MAX(age) as max_age
        FROM students
        GROUP BY grade
        ORDER BY grade
    """, engine)
    print("\nStatistics by grade:")
    print(grade_stats)
    
    # 7. Create enrollment relationship table
    print("\n" + "="*60)
    print("Creating relationship table:")
    
    # Sample enrollment data
    enrollment_data = {
        'enrollment_id': range(1, 11),
        'student_id': [1, 1, 2, 2, 3, 3, 4, 5, 5, 6],
        'course_id': [101, 102, 101, 103, 102, 104, 101, 105, 101, 102],
        'semester': ['Fall 2024'] * 10,
        'grade_received': ['A', 'A-', 'B+', 'B', 'A', 'B+', 'C', 'A-', 'B', 'A']
    }
    
    enrollment_df = pd.DataFrame(enrollment_data)
    enrollment_df.to_sql('enrollments', engine, if_exists='replace', index=False)
    
    print("Enrollment data:")
    print(enrollment_df)
    
    # 8. JOIN operations
    print("\n" + "="*60)
    print("JOIN Operations:")
    
    # Complex JOIN with multiple tables
    detailed_enrollments = pd.read_sql_query("""
        SELECT 
            s.name as student_name,
            s.gpa as student_gpa,
            c.course_name,
            c.credits,
            c.instructor,
            e.grade_received,
            e.semester
        FROM students s
        JOIN enrollments e ON s.student_id = e.student_id
        JOIN courses c ON e.course_id = c.course_id
        WHERE s.is_active = true
        ORDER BY s.name, c.course_name
    """, engine)
    print("\nDetailed enrollment information:")
    print(detailed_enrollments)
    
    # 9. Data manipulation and updates
    print("\n" + "="*60)
    print("Data Updates:")
    
    # Update using pandas and SQLAlchemy
    # First, read current data
    current_students = pd.read_sql_query("SELECT * FROM students", engine)
    
    # Modify the DataFrame
    current_students.loc[current_students['name'] == 'Alice Johnson', 'gpa'] = 4.0
    current_students.loc[current_students['name'] == 'Alice Johnson', 'grade'] = 'A+'
    
    # Write back to database
    current_students.to_sql('students', engine, if_exists='replace', index=False)
    
    # Verify update
    updated_alice = pd.read_sql_query("""
        SELECT name, gpa, grade FROM students WHERE name = 'Alice Johnson'
    """, engine)
    print("\nAfter updating Alice's GPA:")
    print(updated_alice)
    
    # 10. PostgreSQL specific data types
    print("\n" + "="*60)
    print("PostgreSQL Specific Features:")
    
    # Create a table with PostgreSQL-specific types
    special_data = {
        'id': [1, 2, 3],
        'json_data': [
            '{"skills": ["Python", "SQL"], "level": "advanced"}',
            '{"skills": ["Java", "C++"], "level": "intermediate"}',
            '{"skills": ["JavaScript", "React"], "level": "beginner"}'
        ],
        'tags': [
            ['programming', 'database'],
            ['software', 'development'],
            ['web', 'frontend']
        ]
    }
    
    special_df = pd.DataFrame(special_data)
    
    # For arrays, we need to use raw SQL
    with engine.connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS special_features (
                id INTEGER PRIMARY KEY,
                json_data JSONB,
                tags TEXT[]
            )
        """)
        
        # Insert data with proper array formatting
        for _, row in special_df.iterrows():
            conn.execute("""
                INSERT INTO special_features (id, json_data, tags) 
                VALUES (%s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                json_data = EXCLUDED.json_data,
                tags = EXCLUDED.tags
            """, (row['id'], row['json_data'], row['tags']))
        
        conn.commit()
    
    # Query JSON data
    json_query = pd.read_sql_query("""
        SELECT 
            id,
            json_data->>'level' as skill_level,
            json_data->'skills' as skills_json,
            tags
        FROM special_features
    """, engine)
    print("\nJSON and Array data:")
    print(json_query)
    
    # 11. Performance optimization
    print("\n" + "="*60)
    print("Performance Tips:")
    
    # Using chunksize for large datasets
    chunk_size = 1000
    print(f"Reading data in chunks of {chunk_size} rows...")
    
    for chunk in pd.read_sql_query(
        "SELECT * FROM students", 
        engine, 
        chunksize=2  # Small chunk for demonstration
    ):
        print(f"Processing chunk with {len(chunk)} rows")
        # Process each chunk here
        
    # 12. Database schema information
    print("\n" + "="*60)
    print("Database Schema Information:")
    
    # List all tables
    tables = pd.read_sql_query("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
        ORDER BY table_name
    """, engine)
    print("\nTables in database:")
    print(tables)
    
    # Get column information
    columns_info = pd.read_sql_query("""
        SELECT 
            table_name,
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position
    """, engine)
    print("\nColumn information:")
    print(columns_info)
    
    # 13. Backup and export
    print("\n" + "="*60)
    print("Data Export:")
    
    # Export to CSV
    students_export = pd.read_sql_query("SELECT * FROM students", engine)
    students_export.to_csv('students_backup.csv', index=False)
    print("Students data exported to 'students_backup.csv'")
    
    print("\n" + "="*60)
    print("Key PostgreSQL + Pandas Concepts:")
    print("• Use SQLAlchemy engine for better pandas integration")
    print("• PostgreSQL supports advanced data types (JSON, arrays)")
    print("• Window functions provide powerful analytics capabilities")
    print("• Use method='multi' for faster bulk inserts")
    print("• Always use parameterized queries for security")
    print("• PostgreSQL excels at complex queries and large datasets")
    print("• Consider connection pooling for production applications")

except Exception as e:
    print(f"Error: {e}")
    print("\nMake sure PostgreSQL is running and credentials are correct.")
    print("Create the database first: CREATE DATABASE education_db;")
    
finally:
    # Clean up connections
    if 'engine' in locals():
        engine.dispose()
        print("\nDatabase connections closed.")

# Installation requirements:
print("\n" + "="*60)
print("Required packages:")
print("pip install pandas psycopg2-binary sqlalchemy")
print("\nPostgreSQL setup:")
print("1. Install PostgreSQL")
print("2. Create database: CREATE DATABASE education_db;")
print("3. Update connection parameters in the code")
print("4. Ensure PostgreSQL service is running")