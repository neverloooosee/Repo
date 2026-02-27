import os
from datetime import datetime, timedelta
def make_commit(days_ago):
    date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%dT12:00:00')
    os.system(f'echo "pixel" > pixel.txt')
    os.system(f'git add pixel.txt')
    os.system(f'GIT_AUTHOR_DATE={date} GIT_COMMITTER_DATE={date} git commit -m "pixel"')


print("Готово! Тепер роби git push")
