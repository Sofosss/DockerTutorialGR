import logging 
import logging.config
import os

# Get the log file path from the environment variable or use a default path
LOG_FILENAME = os.environ.get('LOGS_PATH', '/var/log/webserver/requests_activity.log')

# Logging configuration settings
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] {%(clientip)s} %(endpoint)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'file': {
            'level': 'CRITICAL',  # Set the logging level to CRITICAL
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': LOG_FILENAME,
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'CRITICAL',  # Set the logging level to CRITICAL
            'propagate': False,
        },
    },
}

# Configure the logging system using the specified settings
logging.config.dictConfig(LOGGING_CONFIG)

# Get the logger for the current module (__name__)
requests_logger = logging.getLogger(__name__)