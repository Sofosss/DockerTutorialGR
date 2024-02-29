import logging 
import logging.config
import os

LOG_FILENAME = os.environ.get('LOGS_PATH', '/var/log/webserver/requests_activity.log')


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'standard': {
            'format': '%(asctime)s [%(levelname)s] {%(clientip)s} %(endpoint)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'file': {
            'level': 'CRITICAL',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': LOG_FILENAME,
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'CRITICAL',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

requests_logger = logging.getLogger(__name__)