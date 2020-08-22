import sys

import argparse

import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
    
from semawal.node import Node
n = Node(
    name="My node", 
    props={"type":"name", "position":1},
    type="root")
n.rename("test node")

n1 = Node(name="Node 1", props={"p1": "v1", "p2": "v2"}, type="root")
n2 = Node(name="Node 2")
n3 = Node("Node 3")
n4 = Node(name="Node 4")

n4.link("h1", n1, power=7)
n4.link("h2", n2, mode=0)
n4.link("h3", n3)
print(n4.getConnections(attributes=["h1"], minPower=5))
print(n4.getLinksAttributes())
print(n4.getRelationesWith(n1))
n4.showLinks()
#######################################################################################"

print("Phase 1 #############################################")
n3.extends(n1)
n3.link(attribute="test", node=n2, power=3)
n1.link(attribute="test", node=n2, power=5)
n3.showLinks()
print("Phase 2 #############################################")
n3.link(attribute="test", node=n2, power=7)
#n1.reset()
#n3.reset()
n3.showLinks()
print("Phase 3 #############################################")
n1.extends(n4)
n4.link("is_a", n2)
n3.showLinks()"