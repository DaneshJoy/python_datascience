"""
پروژه‌ی ۳: ایجاد داده با NumPy، آنالیز و نمایش با Matplotlib
مرور: آرایه‌های NumPy، توابع آماری، ماسک بولی، try/except، رسم نمودار
"""

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None
    print("⚠️ Matplotlib نصب نیست؛ فقط بخش آنالیز اجرا می‌شود.")
    print("   نصب با: pip install matplotlib")

# تولید داده‌ی نمونه: دمای ۳۰ روز، با کمی نوسان تصادفی حول یک میانگین
np.random.seed(42)  # برای یکسان بودن نتایج در هر بار اجرا
days = np.arange(1, 31)
base_temp = 22
temperatures = np.round(base_temp + np.random.normal(loc=0, scale=4, size=30), 1)

# ------- آنالیز داده -------
print("=== آنالیز دمای یک ماه ===")
print(f"میانگین: {temperatures.mean():.1f}°C")
print(f"بیشینه:  {temperatures.max():.1f}°C  (روز {days[temperatures.argmax()]})")
print(f"کمینه:   {temperatures.min():.1f}°C  (روز {days[temperatures.argmin()]})")
print(f"انحراف معیار: {temperatures.std():.2f}")

hot_days = days[temperatures > 25]
print(f"تعداد روزهای گرم‌تر از ۲۵ درجه: {len(hot_days)}")

# ------- نمایش نموداری -------
if plt is not None:
    plt.figure(figsize=(9, 4))
    plt.plot(days, temperatures, marker="o", color="#1F4E79", label="دمای روزانه")
    plt.axhline(temperatures.mean(), color="#C98A22", linestyle="--", label="میانگین")
    plt.title("دمای روزانه در یک ماه")
    plt.xlabel("روز")
    plt.ylabel("دما (°C)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("temperature_chart.png")
    print("\n📊 نمودار در فایل temperature_chart.png ذخیره شد.")
    plt.show()
