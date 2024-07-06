# -*- coding: utf-8 -*-
"""
@Time ： 2024/5/9 15:28
@Auth ： flq
@File ：common_logger.py
@IDE ：PyCharm
"""

import logging
from loguru import logger
from logging import config

# logger = logging.getLogger('django')

import os.path


# 1.🎖️先声明一个类继承logging.Handler(制作一件品如的衣服)
class InterceptTimedRotatingFileHandler(logging.Handler):
    """
    自定义反射时间回滚日志记录器
    缺少命名空间
    """

    def __init__(self, filename, when='d', interval=1, backupCount=15, encoding="utf-8", delay=False, utc=False,
                 atTime=None, logging_levels="all"):
        super(InterceptTimedRotatingFileHandler, self).__init__()
        filename = os.path.abspath(filename)
        when = when.lower()
        # 2.🎖️需要本地用不同的文件名做为不同日志的筛选器
        self.logger_ = logger.bind(sime=filename)
        self.filename = filename
        key_map = {
            'h': 'hour',
            'w': 'week',
            's': 'second',
            'm': 'minute',
            'd': 'day',
        }
        # 根据输入文件格式及时间回滚设立文件名称
        rotation = "%d %s" % (interval, key_map[when])
        retention = "%d %ss" % (backupCount, key_map[when])
        time_format = "{time:%Y-%m-%d_%H-%M-%S}"
        if when == "s":
            time_format = "{time:%Y-%m-%d_%H-%M-%S}"
        elif when == "m":
            time_format = "{time:%Y-%m-%d_%H-%M}"
        elif when == "h":
            time_format = "{time:%Y-%m-%d_%H}"
        elif when == "d":
            time_format = "{time:%Y-%m-%d}"
        elif when == "w":
            time_format = "{time:%Y-%m-%d}"
        level_keys = ["info"]
        # 3.🎖️构建一个筛选器
        levels = {
            "debug": lambda x: "DEBUG" == x['level'].name.upper() and x['extra'].get('sime') == filename,
            "error": lambda x: "ERROR" == x['level'].name.upper() and x['extra'].get('sime') == filename,
            "info": lambda x: "INFO" == x['level'].name.upper() and x['extra'].get('sime') == filename,
            "warning": lambda x: "WARNING" == x['level'].name.upper() and x['extra'].get('sime') == filename}
        # 4. 🎖️根据输出构建筛选器
        if isinstance(logging_levels, str):
            if logging_levels.lower() == "all":
                level_keys = levels.keys()
            elif logging_levels.lower() in levels:
                level_keys = [logging_levels]
        elif isinstance(logging_levels, (list, tuple)):
            level_keys = logging_levels
        for k, f in {_: levels[_] for _ in level_keys}.items():

            # 5.🎖️为防止重复添加sink，而重复写入日志，需要判断是否已经装载了对应sink，防止其使用秘技：反复横跳。
            filename_fmt = filename.replace(".log", "_%s_%s.log" % (time_format, k))
            # noinspection PyUnresolvedReferences,PyProtectedMember
            file_key = {_._name: han_id for han_id, _ in self.logger_._core.handlers.items()}
            filename_fmt_key = "'{}'".format(filename_fmt)
            if filename_fmt_key in file_key:
                continue
                # self.logger_.remove(file_key[filename_fmt_key])
            self.logger_.add(
                filename_fmt,
                retention=retention,
                encoding=encoding,
                level=self.level,
                rotation=rotation,
                compression="tar.gz",  # 日志归档自行压缩文件
                delay=delay,
                enqueue=True,
                filter=f,
            )

    def emit(self, record):
        try:
            level = self.logger_.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 3
        # 6.🎖️把当前帧的栈深度回到发生异常的堆栈深度，不然就是当前帧发生异常而无法回溯
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        self.logger_.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def simple_log_injector(conf):
    """
    对内置日志进行反射
    修改默认的logging root输出
    """
    config.dictConfig(conf)
    logging.setLoggerClass(logging.getLogger('django').__class__)
    logging.root = logging.getLogger('django')
