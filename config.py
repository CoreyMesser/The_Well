import os
from system_constants import SystemConstants


class Config(object):
    DATABASE_URI = os.environ.get(SystemConstants.DATABASE_URI)
