# Support for size-prefixed messages.
#
# Commentary:  In the Raft project, different servers are going to send
# messages to each other.  It is critical that each message stays
# intact as a single object as opposed to being fragmented in
# some way.
#
# There are many ways that this could be achieved.  You could use
# some kind of high-level messages library/framework.  For example,
# ZeroMQ or some kind of Web API,  etc.  You could also
# program it directly using sockets or some low-level code.
# The key thing: messages must be sent and received.


def send_message(sock, msg: bytes):
    size = b"%10d" % len(msg)
    sock.sendall(size)
    sock.sendall(msg)


def recv_exactly(sock, nbytes: int) -> bytes:
    chunks = []
    while nbytes > 0:
        chunk = sock.recv(nbytes)
        if chunk == b"":
            raise IOError("Incomplete message")
        chunks.append(chunk)
        nbytes -= len(chunk)
    return b"".join(chunks)


def recv_message(sock):
    size = int(recv_exactly(sock, 10))
    return recv_exactly(sock, size)
