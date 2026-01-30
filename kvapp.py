#
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


    def run_command(self, cmd: str) -> str:
        match cmd.split():
            case ['get', key]:
                return self._data.get(key, '')
            case ['set', key, value]:
                self._data[key] = value
                return "ok"
            case ['delete', key]:
                if key in self._data:
                    del self._data[key]
                return "ok"
            case _:
                return "error: bad command"

    # Method used by the network code to handle messages in/out
    def execute_command(self, msg: bytes) -> bytes:
        return self.run_command(msg.decode('utf-8')).encode('utf-8')

    def get(self, key: str):
        return self._data.get(key)

    def set(self, key: str, value: str):
        self._data[key] = value
    
    def delete(self, key: str):
        del self._data[key]


# app should be testable
# python3 -m pytest kvapp.py
def test_kvapp():
    kv = KVApp()
    assert kv.set('flower', "sunflower") == "ok"
    assert kv.get('flower') == "sunflower"
    assert kv.get("lily") == ""
    assert kv.delete('flower') == "ok"
    assert kv.get("name") == ""

if __name__ == "__main__":
    test_kvapp()