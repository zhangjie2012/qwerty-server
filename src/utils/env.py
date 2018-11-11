import os
import yaml

config_data = {}


def load_config():
    global config_data

    config_path = os.environ.get('CONFIG_FILE', '/etc/qwerty.yml')
    s = open(config_path, 'r')
    config_data = yaml.load(s)


def get_db_config():
    db_name = config_data['db']['name']
    db_user = config_data['db']['user']
    db_passwd = config_data['db']['passwd']
    db_host = config_data['db']['host']
    db_port = config_data['db']['port']
    return db_name, db_user, db_passwd, db_host, db_port


def get_log_path():
    return config_data['log']['path']


def get_site_info():
    return config_data['site']
