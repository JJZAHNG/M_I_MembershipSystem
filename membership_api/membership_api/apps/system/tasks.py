import subprocess
import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'membership_api.settings.dev')
from django.conf import settings

from celery import shared_task


@shared_task
def backup_database():
    db_name = settings.DATABASES['default']['NAME']

    backup_dir = settings.BASE_DIR / 'sql_backup'  # 获取脚本所在目录的绝对路径
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    backup_name = f'{db_name}_{timestamp}.sql'
    backup_file = os.path.join(backup_dir, backup_name)

    cmd = [
        'mysqldump',
        '--user=' + settings.DATABASES['default']['USER'],
        '--host=' + settings.DATABASES['default']['HOST'],
        '--port=' + str(settings.DATABASES['default']['PORT']),
        '--password=' + settings.DATABASES['default']['PASSWORD'],
        settings.DATABASES['default']['NAME'],
        '--result-file=' + backup_file,
        '--single-transaction',  # 用于InnoDB，保证一致性备份
        '--quick',  # 加快备份速度
        '--lock-tables=false',  # 禁止锁定表，允许同时进行备份和数据库操作
    ]

    # 执行命令
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
