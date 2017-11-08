/var/www/demo/demo.wsgi
import sys, os
sys.path.insert(0, "/var/www/demo")

from demo import app as application
