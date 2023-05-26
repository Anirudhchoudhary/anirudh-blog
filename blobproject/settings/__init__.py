import os
env = os.environ.get("ENV_TYPE")
print(env)
if not env:
    from .devel import *
else:
    from .prod import *