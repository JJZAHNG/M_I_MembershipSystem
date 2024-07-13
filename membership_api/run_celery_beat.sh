#!/bin/bash

# 启动 beat
celery -A membership_api.main_celery beat -l debug &
BEAT_PID=$!
wait

# 当按下 Ctrl+C 时，捕获信号并杀死所有子进程
trap "kill $BEAT_PID" SIGINT
# 保持脚本运行，直到按下 Ctrl+C
while true; do
  sleep 1
done
