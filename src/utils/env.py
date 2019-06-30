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


class UserConfig:
    def init(self, config):
        self.avatar = config['avatar']
        self.nickname = config['nickname']
        self.email = config['email']
        self.github = config['github']
        self.social = config['social']
        self.title = config['title']
        self.career = config['career']
        self.city = config['city']

        # social check
        for item in self.social:
            item['label'], item['link']

    def to_dict(self):
        return {
            'avatar': self.avatar,
            'nickname': self.nickname,
            'email': self.email,
            'github': self.github,
            'social': self.social,
            'title': self.title,
            'career': self.career,
            'city': self.city,
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


server_config = ServerConfig()
user_config = UserConfig()
site_config = SiteConfig()
db_config = DBConfig()
log_config = LogConfig()


def load_config():
    global server_config, user_config, site_config, db_config, log_config

    config_path = os.environ.get('CONFIG_FILE', '/etc/qwerty.yml')
    s = open(config_path, 'r')
    config_data = yaml.safe_load(s)

    server_config.init(config_data['server'])
    user_config.init(config_data['user'])
    site_config.init(config_data['site'])
    db_config.init(config_data['db'])
    log_config.init(config_data['log'])
