"""
This module is a simple key-value store that will serve as the
replicated state machine in the Raft consensus algorithm.
- "state machine" that process commands
- Commands are applied in the same order on all replicas
"""


#
# Raft is focused on the problem of creating a replicated application
# The exact "application" doesn't really matter, but we ahve to have
# something to start. and so will be using a key-value database


class KVApp:
    def __init__(self):
        self._data = {}
    
    # Considerations
    #   - what type of data is stored?
    #   - How are errors handled?
    #   - What gets returned?
    # Should I be thinking about the network here or elsewhere?

    # a network application reeives commands
    # from the network and send responses back on the network


    # Method called by the network code to handle messages in/out
    # Any decoding/encoding of messages takes place in here
    # a wrapper that does message encoding/decoding
    # dont care where it came from, just decode it and send it out
    # meant to connect up with the network layer
    # messages come in as bytes and go out as bytes
    # we could use JSON or something more complex here
    def execute_command(self, msg: str) -> str:
        try:
            cmd = msg.decode('utf-8')
        except UnicodeDecodeError:
            return b'error: invalid UTF-8 encoding'
        
        parts = cmd.split()
        match parts:
            case ['get', key]:
                response = self.get(key)
            case ['set', key, value]:
                response = self.set(key, value)
            case ['delete', key]:
                response = self.delete(key)
            case ['exists', key]:
                response = self.exists(key)
            case ['keys']:
                response = self.keys()
            case _:
                response = f"error: unknown command '{cmd}'"
        
        return response.encode('utf-8')

    def get(self, key: str):
        return self._data.get(key)

    def set(self, key: str, value: str):
        self._data[key] = value
    
    def delete(self, key: str):
        if key in self._data:
            del self._data[key]
            return "ok"
        return "error: key not found"

# app should be testable
# python3 -m pytest kvapp.py
def test_kvapp():
    kv = KVApp()
    assert kv.set('flower', "sunflower") == "ok"
    assert kv.get('flower') == "sunflower"
    assert kv.get("lily") == ""
    assert kv.delete('flower') == "ok"
    assert kv.get("name") == ""

def test_kvapp_messages():
    kv = KVApp()
    assert kv.execute_command(b'set color blue') == b'ok'
    assert kv.execute_command(b'get color') == b'blue'
    assert kv.execute_command(b'delete color') == b'ok'
    assert kv.execute_command(b'get color') == b''
    assert kv.execute_command(b'unknown command') == b'error: bad command'


if __name__ == "__main__":
    test_kvapp()
    test_kvapp_messages()