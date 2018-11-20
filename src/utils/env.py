import os
import yaml


class ServerConfig:
    def init(self, config):
        self.debug = config['debug']
        self.token = config['token']
        self.allowed_hosts = config['allowed_hosts']


class SiteConfig:
    def init(self, config):
        self.title = config['title']
        self.copyright = config['copyright']
        self.ICP = config['ICP']

    def to_dict(self):
        return {
            'title': self.title,
            'copyright': self.copyright,
            'ICP': self.ICP,
        }


class DBConfig:
    def init(self, config):
        self.name = config['name']
        self.user = config['user']
        self.passwd = config['passwd']
        self.host = config['host']
        self.port = config['port']


class LogConfig:
    def init(self, config):
        self.level = config['level']
        self.filepath = config['filepath']
        self.max_bytes = config['max_bytes']
        self.backup_count = config['backup_count']


class BackupConfig:
    def init(self, config):
        self.path = config['path']


server_config = ServerConfig()
site_config = SiteConfig()
db_config = DBConfig()
log_config = LogConfig()
backup_config = BackupConfig()


def load_config():
    global server_config, site_config, db_config, log_config

    config_path = os.environ.get('CONFIG_FILE', '/etc/qwerty.yml')
    s = open(config_path, 'r')
    config_data = yaml.load(s)

    server_config.init(config_data['server'])
    site_config.init(config_data['site'])
    db_config.init(config_data['db'])
    log_config.init(config_data['log'])
    backup_config.init(config_data['backup'])
