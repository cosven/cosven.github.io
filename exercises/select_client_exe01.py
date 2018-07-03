import selectors
import socket

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read_cb)


def read_cb(conn, mask):
    data = conn.recv(8)
    print(data)
    if data == b'':
        conn.close()


sock = socket.socket()
sock.connect(('wen-v1.dev.rack.zhihu.com', 5000))
sock.send(b'GET / HTTP/1.0\r\n\r\n')
# sock.send(b'sub topic.live_lyric\n')
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, read_cb)


loop_count = 0

while True:
    loop_count += 1
    print('loop count', loop_count)
    events = sel.select()
    print('events count', len(events))
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
