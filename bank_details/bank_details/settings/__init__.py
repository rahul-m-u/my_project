def get_env():
    import os

    dir_name = os.path.dirname(__file__)
    path = os.path.join(dir_name, '.env')
    if not os.path.exists(path):
        raise SystemExit(".django-env is not present. Please create one.")

    fp = open(path)
    mode = fp.read().strip()
    fp.close()

    return mode


ENV = get_env()

if ENV == 'development':
    from .dev import *

elif ENV == 'production':
    from .prod import *

else:
    raise SystemExit("Invalid Application Environment")

