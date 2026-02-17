import os
from datetime import datetime, timedelta

# Налаштування: кожне число - це зміщення в днях від початкової дати
# Сітка GitHub має 7 рядків (пн-нд). Ми "малюємо" попіксельно.
def make_commit(days_ago):
    date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%dT12:00:00')
    os.system(f'echo "pixel" > pixel.txt')
    os.system(f'git add pixel.txt')
    os.system(f'GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit -m "pixel"')

# Приблизна мапа для слова SEX (координати в сітці)
# Вам потрібно вирахувати дні. Наприклад, сьогоднішній стовпчик - це 0-6 днів тому.
# Кожен стовпчик вліво - це ще +7 днів.
pixels = [
    # Тут мають бути розраховані індекси днів для літер S, E, X
    # Це спрощений приклад:
    7, 14, 21, 28, 35 # Просто лінія для тесту
]

for p in pixels:
    # Робимо по 10 коммітів на "піксель", щоб він був яскраво-зеленим
    for _ in range(10):
        make_commit(p)

print("Готово! Тепер роби git push")