"""
پروژه‌ی ۲: محاسبه‌گر BMI با گزارش کامل
مرور: توابع، try/except، حلقه‌ی while (برای دریافت مجدد ورودی معتبر)، شرط، f-string
"""


def get_positive_number(prompt):
    """یک عدد مثبت از کاربر می‌گیرد؛ تا زمانی که معتبر نباشد، دوباره می‌پرسد."""
    while True:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            print("⚠️ این یک عدد معتبر نیست. دوباره تلاش کنید.")
            continue

        if value <= 0:
            print("⚠️ لطفاً عددی بزرگ‌تر از صفر وارد کنید.")
            continue

        return value


def bmi_status(bmi):
    if bmi < 18.5:
        return "کمبود وزن"
    elif bmi < 25:
        return "طبیعی"
    elif bmi < 30:
        return "اضافه‌وزن"
    else:
        return "چاق"


def calculate_and_report():
    weight = get_positive_number("وزن خود را به کیلوگرم وارد کنید: ")
    height = get_positive_number("قد خود را به متر وارد کنید (مثلاً 1.72): ")

    bmi = weight / height ** 2
    status = bmi_status(bmi)

    print("\n--- گزارش BMI ---")
    print(f"وزن: {weight:.1f} کیلوگرم")
    print(f"قد: {height:.2f} متر")
    print(f"BMI: {bmi:.2f}")
    print(f"وضعیت: {status}")
    print("------------------")


if __name__ == "__main__":
    print("=== محاسبه‌گر شاخص توده‌ی بدنی (BMI) ===\n")

    while True:
        calculate_and_report()
        again = input("\nمحاسبه برای فرد دیگری هم انجام شود؟ (y/n): ").strip().lower()
        if again != "y":
            print("ممنون که استفاده کردید 🐍")
            break
        print()
