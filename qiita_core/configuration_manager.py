# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

from os.path import join, dirname, abspath
from os import environ

try:
    # Python 2
    from ConfigParser import ConfigParser, NoOptionError
except ImportError:
    # Python 3
    from configparser import ConfigParser, NoOptionError


class ConfigurationManager(object):
    """Holds the QIITA configuration

    Parameters
    ----------
    conf_fp: str, optional
        Filepath to the configuration file. Default: config_test.txt

    Attributes
    ----------
    test_environment : bool
        If true, we are in a test environment.
    base_data_dir : str
        Path to the base directorys where all data file are stored
    user : str
        The postgres user
    password : str
        The postgres password for the previous user
    database : str
        The postgres database to connect to
    host : str
        The host where the database lives
    port : int
        The port used to connect to the postgres database in the previous host
    """
    def __init__(self):
        # If conf_fp is None, we default to the test configuration file
        try:
            conf_fp = environ['QIITA_CONFIG_FP']
        except KeyError:
            conf_fp = join(dirname(abspath(__file__)),
                           'support_files/config_test.txt')

        # Parse the configuration file
        config = ConfigParser()
        with open(conf_fp, 'U') as conf_file:
            config.readfp(conf_file)

        # Get the configuration of the main section
        self.test_environment = config.getboolean('main', 'TEST_ENVIRONMENT')
        try:
            self.base_data_dir = config.get('main', 'BASE_DATA_DIR')
        except NoOptionError as e:
            if self.test_environment:
                self.base_data_dir = join(dirname(abspath(__file__)),
                                          '../test_data')
            else:
                raise e

        # Get the configuration of the postgres section
        self.user = config.get('postgres', 'USER')
        try:
            self.password = config.get('postgres', 'PASSWORD')
        except NoOptionError as e:
            if self.test_environment:
                self.password = None
            else:
                raise e
        self.database = config.get('postgres', 'DATABASE')
        self.host = config.get('postgres', 'HOST')
        self.port = config.getint('postgres', 'PORT')
