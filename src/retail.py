import psycopg2

# اطلاعات اتصال به دیتابیس
dbname = 'postgres'  # نام دیتابیس
user = 'postgres'  # نام کاربری (در اکثر مواقع postgres است)
password = 'lham7169'  # پسورد
host = 'localhost'  # آدرس میزبان (برای اتصال محلی از localhost استفاده می‌شود)
port = '5432'  # پورت پیش‌فرض PostgreSQL

try:
    # اتصال به دیتابیس
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # ایجاد یک کرسر برای اجرای دستورات SQL
    cursor = connection.cursor()

    # اجرای یک پرس و جو ساده (خواندن داده‌ها از یک جدول)
    cursor.execute("SELECT * FROM stores ;")

    # نمایش نتایج
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # بستن کرسر و اتصال به دیتابیس
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error: {error}")
