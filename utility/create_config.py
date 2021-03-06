import os
from configparser import ConfigParser


def write_config():
    project_path = os.path.join(os.path.dirname(__file__), '..')
    config_path = os.path.join(project_path, 'config.ini')

    config = ConfigParser()

    config['globals'] = {'progname': 'ItMakesCoffee',
                         'progversion': '2020.05.28.01'
                         }

    config['paths'] = {'icons': os.path.join(project_path, 'icons'),
                       'last_data': 'C:\\Users\\amwae\\Python\\Lambda\\test\\03-04-2020',
                       'last_save': 'C:\\Users\\amwae\\Python\\ItMakesCoffee'
                       }

    with open(config_path, 'w') as f:
        config.write(f)
