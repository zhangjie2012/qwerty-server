import os


def get_db_config():
    db_name = os.environ.get('DB_NAME', 'qwerty')
    db_user = os.environ.get('DB_USER', 'qwerty_user')
    db_passwd = os.environ.get('DB_PASSWD', 'qwerty_passwd')
    db_host = os.environ.get('DB_HOST', 'localhost')
    db_port = os.environ.get('DB_PORT', '3306')
    return db_name, db_user, db_passwd, db_host, db_port


def get_log_path():
    log_path = os.environ.get('LOG_FILE', '/data/log/qwerty.log')
    return log_path
