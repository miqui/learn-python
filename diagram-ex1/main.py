from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


def do_diagram():
    with Diagram("Grouped Workers", show=False, direction="TB"):
        ELB("lb") >> [EC2("worker1"),
                      EC2("worker2"),
                      EC2("worker3"),
                      EC2("worker4"),
                      EC2("worker5")] >> RDS("events")


if __name__ == '__main__':
    do_diagram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
