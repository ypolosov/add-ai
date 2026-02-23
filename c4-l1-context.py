"""
C4 Level 1 — System Context (diagrams as code).
Uses diagrams.c4 for System, SystemBoundary, Relationship; Custom with person icon for people.
"""
import os
from urllib.request import urlretrieve

from diagrams import Diagram, Cluster
from diagrams.c4 import System, SystemBoundary, Relationship
from diagrams.custom import Custom

# Person icon (downloaded once, reused for all Person nodes). PNG for Graphviz.
_script_dir = os.path.dirname(os.path.abspath(__file__))
_icons_dir = os.path.join(_script_dir, "icons")
PERSON_ICON = os.path.join(_icons_dir, "person.png")
os.makedirs(_icons_dir, exist_ok=True)
if not os.path.exists(PERSON_ICON):
    urlretrieve(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/User_icon_2.svg/240px-User_icon_2.svg.png",
        PERSON_ICON,
    )


def Person(label: str, _description: str = "") -> Custom:
    """Person node with people icon (Custom node)."""
    return Custom(label, PERSON_ICON)


graph_attr = {"splines": "spline"}

with Diagram(
    "C4 L1 — System Context",
    direction="LR",
    show=False,
    filename="c4-l1-context",
    graph_attr=graph_attr,
):
    # Platform staff
    with Cluster("Platform staff"):
        platform_admin = Person("Platform admin", "Manages platform")
        platform_employee = Person("Platform employee", "Uses platform")

    # Operator staff
    with Cluster("Operator staff"):
        operator_admin = Person("Operator admin", "Manages operator")
        operator_employee = Person("Operator employee", "Uses operator")

    # Casino end-users
    with Cluster("Casino end-users"):
        player = Person("Player", "Plays games")
        visitor = Person("Visitor", "Visits casino")

    # Platform maintainers
    with Cluster("Platform maintainers"):
        developer = Person("Developer", "Develops")
        devops = Person("Devops", "Operations")
        designer = Person("Designer", "Designs")
        tester = Person("Tester", "Tests")

    # External systems (C4 external systems)
    with Cluster("External integrations"):
        dns_cdn = System("DNS & CDN Provider API", "DNS and CDN", external=True)
        games = System("Games Provider API", "Game content", external=True)
        payments = System("Payments Provider API", "Payments", external=True)
        fraud = System("Fraud Detection Provider API", "Fraud checks", external=True)
        kyc = System("KYC Provider API", "Identity verification", external=True)
        aml = System("AML Provider API", "Anti-money laundering", external=True)
        cs = System("Customer Support Provider API", "Support", external=True)
        external_nodes = [dns_cdn, games, payments, fraud, kyc, aml, cs]

    # Product instance — B2B2C Gambling Platform (C4 system boundary)
    with SystemBoundary("B2B2C Gambling Platform (Product instance)"):
        b2b2c_platform = System("B2B2C SaaS Platform", "Platform core")
        b2b_operator = System("B2B SaaS Operator", "Operator portal")
        b2c_casino = System("B2C SaaS Casino", "Casino front-end")

    # People → systems
    platform_admin >> Relationship("uses") >> b2b2c_platform
    platform_employee >> Relationship("uses") >> b2b2c_platform
    operator_admin >> Relationship("uses") >> b2b_operator
    operator_employee >> Relationship("uses") >> b2b_operator
    player >> Relationship("uses") >> b2c_casino
    visitor >> Relationship("uses") >> b2c_casino

    # Product systems → external integrations
    b2b2c_platform >> Relationship("integrates") >> external_nodes
    b2b_operator >> Relationship("integrates") >> external_nodes
    b2c_casino >> Relationship("integrates") >> external_nodes

    # Internal platform connections
    b2b2c_platform >> b2b_operator
    b2b2c_platform >> b2c_casino
    b2b_operator >> b2c_casino

    # Maintainers → product
    developer >> Relationship("maintains") >> b2b2c_platform
    devops >> Relationship("maintains") >> b2b2c_platform
    designer >> Relationship("maintains") >> b2b2c_platform
    tester >> Relationship("maintains") >> b2b2c_platform
