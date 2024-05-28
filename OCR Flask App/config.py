import os

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'OCR'

    UPLOADS = r"C:\Users\suraj\OneDrive\Desktop\projects\OCR\OCR Flask App\app\static\uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = True

class DebugConfig(Config):
    DEBUG = False


# note
'''Config Class: The Config class serves as a base configuration class. It defines default configuration options for the application. These options include:

DEBUG: A boolean indicating whether debug mode is enabled (default is False).
TESTING: A boolean indicating whether testing mode is enabled (default is False).
basedir: The absolute path of the directory containing the configuration file.
SECRET_KEY: A secret key used for cryptographic operations, such as session management or CSRF protection.
UPLOADS: The directory where uploaded files are stored.
SESSION_COOKIE_SECURE: A boolean indicating whether the session cookie should only be sent over HTTPS (default is True).
DEFAULT_THEME: An optional default theme for the application.'''