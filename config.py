import toml
config_path = './config.toml'


def load_config():
    config = toml.load(config_path)
    return config
