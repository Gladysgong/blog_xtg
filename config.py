# coding=utf-8
import os
import logging.config
# 全局logging
logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'log.conf'))

redis_session_config = dict(
    db_no=0,
    host="127.0.0.1",
    port=6379,
    password=None,
    max_connections=10,
    session_key_name="TR_SESSION_ID",
    session_expires_days=7,
)

database_config = dict(
    engine_config='postgresql+psycopg2://mhq:1qaz2wsx@localhost:5432/blog',
    sql_echo=True,
)

config = dict(
    debug=True,
    compress_response=True,
    xsrf_cookies=True,
    cookie_secret="kjsdhfweiofjhewnfiwehfneiwuhniu",
    login_url="/auth/login",
    server_port=8888,
    max_threads_num=500,
    database=database_config,
    redis_session=redis_session_config,
)