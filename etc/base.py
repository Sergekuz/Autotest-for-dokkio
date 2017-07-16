import os
import platform

ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
TEST_PATH = os.path.join(ROOT, 'tests')


def project_url():
        return 'https://dokkio.com'

def path_for_artifacts():
    artifacts_path = os.path.abspath(
        os.path.join(
            ROOT,
            'artifacts',
            'artifacts_result'))
    if not os.path.exists(artifacts_path):
        os.makedirs(artifacts_path)
    return artifacts_path


BIN_FOLDER = os.path.abspath(
    os.path.join(
        os.path.dirname(
            __file__,
        ),
        '..',
        'bin',
    ),
)

SELENIUM_EX = {
    'USE_REMOTE': False,
    'POLLING_TIMEOUT': 60,
    'POLLING_DELAY': 0.1,
    'SCRIPT_TIMEOUT': None,
    'IMPLICITLY_WAIT': 65,
    'WINDOW_SIZE': None,
    'MAXIMIZE_WINDOW': True,
    'DEFAULT_BROWSER': 'chrome',
    'PROJECT_URL': project_url(),
    'SCREEN_PATH': path_for_artifacts(),
    'LOGS_PATH': path_for_artifacts(),


    'CHROME': {
        'executable_path': os.path.join(BIN_FOLDER, 'chromedriver'),
        'service_log_path': os.path.join(path_for_artifacts(), 'chromedriver.log'),
    },

    'REMOTE': {
        'CAPABILITIES': {
            'chrome': {
                'version': '41',
            },
        },
        'OPTIONS': {
            'keep_alive': True,
            'command_executor': 'http://localhost:4444/wd/hub',
        },
    },
}


LOGGING_SETTINGS = {
    'version': 1,
    'formatters': {
        'basic': {
            'format': '%(asctime)-15s %(name)s %(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'basic'
        },
        'null': {
            'class': 'logging.NullHandler',
            'level': 'DEBUG'
        },
    },
    'loggers': {
        'steps': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'seismograph': {
            'propagate': True,
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
