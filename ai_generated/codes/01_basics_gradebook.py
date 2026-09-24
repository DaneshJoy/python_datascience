"""
پروژه‌ی ۱: دفترچه‌نمرات کلاس
مرور مفاهیم پایه: متغیر، لیست، دیکشنری، حلقه‌ی for، شرط و f-string
"""

# هر دانش‌آموز یک دیکشنری است؛ همه‌ی دانش‌آموزان در یک لیست جمع شده‌اند
students = [
    {"name": "آرش", "score": 17.5},
    {"name": "نگار", "score": 19.0},
    {"name": "رامین", "score": 9.5},
    {"name": "سارا", "score": 14.0},
]

PASS_SCORE = 10  # یک ثابت ساده: حد نصاب قبولی

print("=" * 30)
print("گزارش نمرات کلاس")
print("=" * 30)

total = 0
passed_count = 0

for student in students:
    name = student["name"]
    score = student["score"]
    total += score

    if score >= PASS_SCORE:
        status = "قبول ✅"
        passed_count += 1
    else:
        status = "مردود ❌"

    print(f"{name} — نمره: {score:.1f} — وضعیت: {status}")

average = total / len(students)
print("-" * 30)
print(f"میانگین کلاس: {average:.2f}")
print(f"تعداد قبول‌شده‌ها: {passed_count} از {len(students)} نفر")

# بخش تعاملی: جست‌وجوی نمره‌ی یک نفر با نام (نمونه‌ای از try/except)
print("\nبرای جست‌وجوی نمره‌ی یک نفر نامش را وارد کنید (برای خروج، Enter خالی بزنید)")

while True:
    name_query = input("نام: ").strip()
    if name_query == "":
        print("خدانگهدار! 👋")
        break

    try:
        found = next(s for s in students if s["name"] == name_query)
        print(f"نمره‌ی {found['name']}: {found['score']}")
    except StopIteration:
        print("چنین دانش‌آموزی در لیست پیدا نشد.")
