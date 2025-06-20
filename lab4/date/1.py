from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("1. Дата пять дней назад:", five_days_ago)

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("2. Вчера:", yesterday)
print("   Сегодня:", today)
print("   Завтра:", tomorrow)

now_no_microseconds = datetime.now().replace(microsecond=0)
print("3. Без микросекунд:", now_no_microseconds)

date1 = datetime(2025, 6, 20, 12, 0, 0)
date2 = datetime(2025, 6, 18, 9, 30, 0)
difference_seconds = int((date1 - date2).total_seconds())
print("4. Разница между двумя датами в секундах:", difference_seconds)