# Heliotrope 🌻
Like sunflowers tracking the sun, Raft nodes follow their leader

## Overview

Heliotrope draws its name from the sun-tracking behavior of sunflowers—standing in ranks and uniformly turning toward the sun—mirroring how Raft achieves consensus through follower nodes orienting toward a single leader.

Heliotrope is a learning project implementing the Raft Concensus Algorithm from the ground up. Built from the ground up, from low-level networking with raw sockets to the Raft algorithm itself.


## Progress

### Phase 1
What we want: 
1. network application that runs kv server
2. client that you can run to interact with that
3. you should be able to give it some commands 
4. hopefully it can handle multiple clients

**key is that our Key-Value is on the network
Where a command goes in and a response goes out

Phase 1 Architecture

![Phase 1 Architecture Diagram](refrences/Phase%201%20Architecture%20Diagram.png)


## Running the System

1. **Start the server**:
```bash
   python kvserver.py
```

2. **Start one or more clients**:
```bash
   python kvclient.py
```

3. **Try some commands**:
```
   kv> set color blue
   ← ok
   kv> set flower sunflower
   ← ok
   kv> get color
   ← blue
```