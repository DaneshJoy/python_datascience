"""
پروژه‌ی ۵ (جایزه): دریافت آنلاین قیمت بیت‌کوین و تحلیل روند
مرور: درخواست اینترنتی (requests)، try/except برای خطای شبکه، pandas، ایجاد دایرکتوری، رسم نمودار

نیازمند: pip install requests
داده از API رایگان CoinGecko گرفته می‌شود (بدون نیاز به کلید/ثبت‌نام).

⚠️ این اسکریپت فقط برای تمرین برنامه‌نویسی است، نه توصیه‌ی مالی یا سرمایه‌گذاری.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import requests
except ImportError:
    requests = None
    print("⚠️ کتابخانه‌ی requests نصب نیست. نصب با: pip install requests")

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
PARAMS = {"vs_currency": "usd", "days": 30}


def fetch_prices():
    """قیمت ۳۰ روز اخیر بیت‌کوین را از CoinGecko می‌گیرد؛ در صورت هر خطایی None برمی‌گرداند."""
    if requests is None:
        return None
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        return response.json()["prices"]  # لیستی از [timestamp_ms, price]
    except requests.exceptions.RequestException as e:
        print(f"⚠️ دریافت داده از اینترنت ناموفق بود: {e}")
        return None
    except (KeyError, ValueError):
        print("⚠️ ساختار پاسخ سرور غیرمنتظره بود.")
        return None


raw_prices = fetch_prices()

if raw_prices:
    df = pd.DataFrame(raw_prices, columns=["timestamp", "price_usd"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df = df.groupby("date", as_index=False)["price_usd"].mean()
    print("✅ داده‌ی واقعی از CoinGecko دریافت شد.")
else:
    print("↩️ به‌جای داده‌ی آنلاین، از یک داده‌ی نمونه (تصادفی) برای دمو استفاده می‌شود.")
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30).date
    prices = 60000 + np.cumsum(np.random.normal(0, 800, size=30))
    df = pd.DataFrame({"date": dates, "price_usd": prices})

# ------- تحلیل ساده -------
df["daily_change_%"] = df["price_usd"].pct_change() * 100
highest = df.loc[df["price_usd"].idxmax()]
lowest = df.loc[df["price_usd"].idxmin()]

print(f"\nبیشترین قیمت: {highest['price_usd']:.0f}$ در {highest['date']}")
print(f"کمترین قیمت: {lowest['price_usd']:.0f}$ در {lowest['date']}")
print(f"میانگین تغییر روزانه: {df['daily_change_%'].mean():.2f}%")

# ------- ذخیره‌ی خروجی در دایرکتوری output -------
csv_path = os.path.join(OUTPUT_DIR, "bitcoin_prices.csv")
df.to_csv(csv_path, index=False)
print(f"📁 داده ذخیره شد: {csv_path}")

# ------- رسم نمودار -------
plt.figure(figsize=(9, 4))
plt.plot(df["date"], df["price_usd"], color="#C98A22")
plt.title("روند قیمت بیت‌کوین (۳۰ روز اخیر)")
plt.xlabel("تاریخ")
plt.ylabel("قیمت (دلار)")
plt.xticks(rotation=45)
plt.tight_layout()

chart_path = os.path.join(OUTPUT_DIR, "bitcoin_trend.png")
plt.savefig(chart_path)
print(f"📊 نمودار ذخیره شد: {chart_path}")
plt.show()
