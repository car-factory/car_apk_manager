import os

"""
# Separate django settings for multiple environments
https://gist.github.com/wonderbeyond/c344accb73a37e1933f2036d4edd0288
"""
# Default to dev for safety.
APP_ENV = os.environ.get('DJANGO_MODE', 'develop')
