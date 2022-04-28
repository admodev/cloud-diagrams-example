from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Web Service", show=False, direction="TB"):
    ELB("Load Balancer") >> EC2("Elastic Compute") >> RDS("Database Service")
    ELB("Load Balancer") >> [EC2("worker 1"),
            EC2("worker 2"),
            EC2("worker 3"),
            EC2("worker 4"),
            EC2("worker 5")] >> RDS("eventos")

