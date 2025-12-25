
## این پروژه شامل پاسخ به سوالات مربوط به تسک شرکت رسمیو است.

برای اجرای پاسخ هر سوال می‌توانید به پوشه‌ی مربوط به سوال مراجعه کرده و سپس فایل main.py را اجرا کنید.

---
# Official newspaper legal ads (Official Gazette) Crawler (rrk.ir)

## Project Structure


    ├── question1/
        └── main.py
    ├── question2/
        └── main.py
    ├── requirements.txt
    └── README.md


---

## Question 1

Open the rrk.ir website using a browser and navigate to the search section.

**Approach:**  
This part demonstrates basic browser automation using Selenium, including:
- Launching the browser then loading the website
- Click on search section

---

## Question 2

Collect Official Gazette advertisements (legal notices) from the last 10 days using the advanced search feature of rrk.ir.

**Approach:**

- Selenium was used due to the dynamic and JavaScript-driven nature of the website.
- Page elements were identified using browser inspection tools (`id` and `class_name`).
- Gregorian dates were calculated using Python’s standard libraries and converted to Jalali (Shamsi) format using the `jdatetime` library.
- Advanced search filters were filled and the search was executed.
- The total number of retrieved advertisements and the total execution time were extracted and reported.


---


## How to Run

1. Install dependencies:
   ```bash
    pip install -r requirements.txt

2. Make sure ChromeDriver is installed and compatible with your Chrome version.

3. Run each question separately:

```bash
    cd Question1
    python main.py
```

```bash
    cd Question2
    python main.py