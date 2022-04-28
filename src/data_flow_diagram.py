from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.storage import S3

with Diagram("Web Services", show=False):
    ELB("LB") >> EC2("web") >> RDS("DB") >> S3("store")
    ELB("LB") >> EC2("web") >> RDS("DB") << EC2("stat")
    (ELB("LB") >> EC2("web")) - EC2("web") >> RDS("DB")
