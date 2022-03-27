#!/usr/bin/env python
# automatically save|load session

from qutescript import userscript


@userscript
def hello_world(request):
    request.send_text('Hello, world!')


if __name__ == '__main__':
    hello_world()
