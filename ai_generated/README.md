# 🐍 پایتون برای علم داده — دوره‌ی مقدماتی

![Language](https://img.shields.io/badge/language-Persian%20(fa)-blue)
![Stack](https://img.shields.io/badge/stack-HTML%2FCSS%2FJS-orange)
![Build](https://img.shields.io/badge/build-not%20required-brightgreen)

یک دوره‌ی مقدماتی و پروژه‌محور برای یادگیری پایتون با رویکرد علم داده — در قالب صفحات وب مستقل (آماده‌ی تدریس یا خودآموزی، بدون نیاز به نصب یا Build) به‌همراه کد کامل و اجراپذیر هر پروژه.

## درباره‌ی دوره

دوره در **۳ جلسه** و **۹ بخشِ یک‌ساعته** پیش می‌رود: از آشنایی و نصب پایتون شروع می‌شود، با متغیرها، شرط‌ها، حلقه‌ها و ساختارهای داده ادامه پیدا می‌کند، و در نهایت به NumPy، Pandas و Matplotlib می‌رسد — همه با پروژه‌های واقعی (محاسبه‌ی BMI، پردازش فایل CSV، رسم نمودار). یک **بخش جایزه‌ی اختیاری** درباره‌ی گرفتن داده از اینترنت (requests) هم به دوره اضافه شده است.

## ویژگی‌های این مخزن

- 📄 هر بخش یک فایل HTML مستقل و کامل — فقط با مرورگر باز می‌شود
- 🌗 دکمه‌ی سوییچ بین تم روشن و تیره
- 🧪 طراحی الهام‌گرفته از سلول‌های نوت‌بوک ژوپیتر برای نمایش کد و خروجی
- 🔤 کاملاً فارسی، راست‌به‌چپ (RTL)
- 🧩 بدون فریم‌ورک یا وابستگی در صفحات آموزشی — فقط HTML، CSS و جاوااسکریپت خالص
- 🐍 کد کامل و اجراپذیر هر پروژه، جدا از اسلایدها، در پوشه‌ی [`projects/`](projects/)

## فهرست بخش‌ها

### جلسه ۱ — مبانی پایتون
| بخش | عنوان | فایل |
|:---:|---|---|
| ۱ | مقدمه، نصب و محیط‌های کدنویسی | [s1-p1-intro-setup.html](s1-p1-intro-setup.html) |
| ۲ | متغیرها، انواع داده و عملگرها | [s1-p2-variables-types.html](s1-p2-variables-types.html) |
| ۳ | شرط‌ها، حلقه‌ها و پروژه‌ی BMI | [s1-p3-conditionals-loops.html](s1-p3-conditionals-loops.html) |

### جلسه ۲ — ساختار داده و کتابخانه‌ها
| بخش | عنوان | فایل |
|:---:|---|---|
| ۴ | لیست‌ها، دیکشنری‌ها و توابع | [s2-p1-collections-functions.html](s2-p1-collections-functions.html) |
| ۵ | نصب کتابخانه‌ها و NumPy | [s2-p2-packages-numpy.html](s2-p2-packages-numpy.html) |
| ۶ | آشنایی با Pandas | [s2-p3-pandas-basics.html](s2-p3-pandas-basics.html) |

### جلسه ۳ — تحلیل و نمایش داده
| بخش | عنوان | فایل |
|:---:|---|---|
| ۷ | پردازش CSV و پروژه‌ی تحلیل داده | [s3-p1-csv-project.html](s3-p1-csv-project.html) |
| ۸ | رسم نمودار با Matplotlib | [s3-p2-matplotlib.html](s3-p2-matplotlib.html) |
| ۹ | پروژه‌ی پایانی و جمع‌بندی | [s3-p3-final-project.html](s3-p3-final-project.html) |

### 🎁 بخش جایزه (اختیاری)
| عنوان | فایل |
|---|---|
| گرفتن داده از اینترنت با requests | [bonus-requests-api.html](bonus-requests-api.html) |

## کدهای پروژه‌ها (Python)

علاوه بر اسلایدهای آموزشی، کد کامل و اجراپذیر هر پروژه در پوشه‌ی [`projects/`](projects/) هم موجود است:

| فایل | خلاصه |
|---|---|
| `01_basics_gradebook.py` | مرور متغیر، لیست، دیکشنری، حلقه و شرط |
| `02_bmi_calculator.py` | محاسبه‌گر BMI با گزارش f-string و دریافت مجدد ورودی معتبر |
| `03_numpy_matplotlib_demo.py` | ساخت و آنالیز داده با NumPy + نمودار با Matplotlib |
| `04_csv_stackoverflow_trends.py` | پردازش CSV، ایجاد دایرکتوری خروجی و ذخیره‌ی نتیجه |
| `05_bonus_crypto_prices.py` | دریافت آنلاین قیمت بیت‌کوین با requests و تحلیل روند |

جزئیات اجرا، پیش‌نیازها و نکات هر اسکریپت در [`projects/README.md`](projects/README.md) آمده است.

## نحوه‌ی استفاده

**برای اسلایدهای آموزشی:**
۱. مخزن را دانلود یا `clone` کنید.
۲. مطمئن شوید پوشه‌ی `assets/` (شامل `style.css` و `script.js`) کنار فایل‌های HTML باقی می‌ماند.
۳. هر فایل را مستقیماً با مرورگر باز کنید — نیازی به سرور یا نصب چیزی نیست.

> 💡 فونت Vazirmatn از گوگل‌فونت‌ها بارگذاری می‌شود، پس برای نمایش دقیق آن به اتصال اینترنت نیاز است. بدون اینترنت هم صفحه با فونت جایگزین سیستم باز می‌شود و کاملاً قابل‌خواندن می‌ماند.

**برای اجرای کدهای پروژه‌ها:**
```bash
cd projects
pip install -r requirements.txt
python 01_basics_gradebook.py
```

## ساختار پوشه‌ها

```
.
├── assets/
│   ├── style.css      # استایل مشترک همه‌ی بخش‌ها
│   └── script.js      # منطق تم روشن/تیره + افکت تایپ کد
├── projects/
│   ├── 01_basics_gradebook.py
│   ├── 02_bmi_calculator.py
│   ├── 03_numpy_matplotlib_demo.py
│   ├── 04_csv_stackoverflow_trends.py
│   ├── 05_bonus_crypto_prices.py
│   ├── requirements.txt
│   └── README.md
├── s1-p1-intro-setup.html
├── s1-p2-variables-types.html
├── s1-p3-conditionals-loops.html
├── s2-p1-collections-functions.html
├── s2-p2-packages-numpy.html
├── s2-p3-pandas-basics.html
├── s3-p1-csv-project.html
├── s3-p2-matplotlib.html
├── s3-p3-final-project.html
└── bonus-requests-api.html
```

## پیش‌نیازها

برای دنبال‌کردن محتوای دوره نیازی به پیش‌زمینه نیست. برای اجرای واقعی مثال‌های کد (نه فقط خواندن)، نصب [Anaconda](https://www.anaconda.com/) پیشنهاد می‌شود — که خودِ نصب آن در بخش ۱ دوره آموزش داده شده است. برای اجرای اسکریپت‌های پوشه‌ی `projects/`، پکیج‌های داخل `requirements.txt` هم لازم است.

## مشارکت

پیشنهاد، اصلاح یا گزارش اشکال دارید؟ خوشحال می‌شویم از طریق Issue یا Pull Request مطرح کنید.

## لایسنس

این مخزن فعلاً بدون لایسنس مشخص منتشر شده است. اگر می‌خواهید شرایط استفاده و بازنشر را برای دیگران روشن کنید، می‌توانید یک فایل `LICENSE` (مثلاً MIT) به مخزن اضافه کنید.

---

ساخته‌شده با 🐍 برای علاقه‌مندان به علم داده.
