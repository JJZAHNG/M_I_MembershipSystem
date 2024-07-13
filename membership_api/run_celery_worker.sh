#!/bin/bash

# 定义启动worker的命令
start_worker() {
    if [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        # 如果是Windows系统（通过MSYS或Cygwin），使用eventlet
        celery -A membership_api.main_celery worker -l debug -P eventlet &
    else
        # 如果是其他Unix-like系统，不使用eventlet
        celery -A membership_api.main_celery worker -l debug &
    fi
    WORKER_PID=$!
}

# 启动 worker
start_worker

# 当按下 Ctrl+C 时，捕获信号并杀死所有子进程
trap "kill $WORKER_PID" SIGINT

# 保持脚本运行，直到按下 Ctrl+C
while true; do
    sleep 1
done
