"""
پروژه‌ی ۴: پردازش داده‌ی روند محبوبیت زبان‌های برنامه‌نویسی در StackOverflow
مرور: pandas، ایجاد دایرکتوری (os.makedirs)، try/except، تبدیل جدول wide→long، ذخیره‌ی خروجی، رسم نمودار

اگر فایل واقعی خودتان را دارید، مقدار INPUT_FILE را به مسیر آن تغییر دهید.
ستون‌های موردانتظار: یک ستون سال (Year) + یک ستون برای هر زبان برنامه‌نویسی
مثال: Year, Python, JavaScript, Java
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "data/stackoverflow_trends.csv"
OUTPUT_DIR = "output"

os.makedirs("data", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(path):
    """فایل CSV را می‌خواند؛ اگر پیدا نشد یا خراب بود، یک نمونه‌ی آزمایشی می‌سازد."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"⚠️ فایل «{path}» پیدا نشد؛ یک نمونه‌ی آزمایشی برای دمو ساخته می‌شود.")
        sample = pd.DataFrame({
            "Year":       [2016, 2018, 2020, 2022, 2024],
            "Python":     [6, 9, 13, 17, 18],
            "JavaScript": [12, 12, 11, 10, 8],
            "Java":       [10, 8, 7, 6, 5],
        })
        sample.to_csv(path, index=False)
        return sample
    except pd.errors.ParserError:
        print("❌ فایل CSV خراب یا ناقص است.")
        raise


df = load_data(INPUT_FILE)
print("داده‌ی خام:")
print(df.head())

# تبدیل از حالت wide (هر زبان یک ستون) به long (هر سطر یک زبان-سال)
long_df = df.melt(id_vars="Year", var_name="Language", value_name="Share")

# تحلیل: میانگین سهم هر زبان در کل بازه‌ی زمانی
summary = (
    long_df.groupby("Language")["Share"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index(name="AverageShare")
)
print("\nمیانگین سهم هر زبان:")
print(summary)

top_language = summary.iloc[0]["Language"]
print(f"\n🏆 پرطرفدارترین زبان در این بازه: {top_language}")

# ------- ذخیره‌ی خروجی‌ها در دایرکتوری output -------
summary_path = os.path.join(OUTPUT_DIR, "language_summary.csv")
summary.to_csv(summary_path, index=False)
print(f"📁 خلاصه‌ی تحلیل ذخیره شد: {summary_path}")

# ------- رسم نمودار روند -------
plt.figure(figsize=(9, 5))
for language in df.columns[1:]:
    plt.plot(df["Year"], df[language], marker="o", label=language)

plt.title("روند محبوبیت زبان‌های برنامه‌نویسی")
plt.xlabel("سال")
plt.ylabel("سهم از پرسش‌ها (%)")
plt.legend()
plt.tight_layout()

chart_path = os.path.join(OUTPUT_DIR, "language_trend.png")
plt.savefig(chart_path)
print(f"📊 نمودار ذخیره شد: {chart_path}")
plt.show()
