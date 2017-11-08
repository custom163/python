import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


host = 'www.google.com'
host2 = 'www.yahoo.com'
test = Resolver()
a = test(host)
c = test(host2)
print(a)
print(c)
