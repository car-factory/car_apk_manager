from car_apk_manager.env import APP_ENV

if APP_ENV in ('ci', 'develop', 'product'):
    exec('from .%s import *' % APP_ENV)
