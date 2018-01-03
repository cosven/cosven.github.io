import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read_cb)


def read_cb(conn, mask):
    pass


sock = socket.socket()
sock.bind(('localhost', 2333))
sock.listen(5)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)


loop_count = 0

while True:
    loop_count += 1
    print('loop count', loop_count)
    events = sel.select()
    print('events count', len(events))
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
