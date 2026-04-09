# Project Configuration

PROJECT_ROOT = '/path/to/project'

# Data Directories
DATA_DIR = f'{PROJECT_ROOT}/data'
LOG_DIR = f'{PROJECT_ROOT}/logs'

# Logging Configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{'
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'my_module': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Database Path
DATABASE_PATH = f'{PROJECT_ROOT}/database.db'

# Crawler Settings
CRAWLER_SETTINGS = {
    'user_agent': 'my_crawler (http://mywebsite.com)',
    'timeout': 30,
}

# Betting Sites Configuration
BETTING_SITES = {
    'site1': {
        'url': 'http://example.com',
        'api_key': 'your_api_key_here',
    },
    'site2': {
        'url': 'http://example2.com',
        'api_key': 'your_api_key_here',
    },
}

# Analysis Parameters
ANALYSIS_PARAMETERS = {
    'param1': 'value1',
    'param2': 'value2',
}