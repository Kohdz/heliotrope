# Heliotrope

## Overview

Heliotrope draws its name from the sun-tracking behavior of sunflowers—standing in ranks and uniformly turning toward the sun—mirroring how Raft achieves consensus through follower nodes orienting toward a single leader.

## Progress

1. Worked out communication between 1 machine and another using sockets
2. create a KV application based on the communication in step 1


Testing KV
1. run `python kvserver.py`
2. run `python kvclient.py` 
3. send the requests