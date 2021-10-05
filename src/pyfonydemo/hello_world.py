import os
from pyfonycore.bootstrap import bootstrapped_container

container = bootstrapped_container.init(os.environ["APP_ENV"])

print(container.get_parameters().foo.bar)
