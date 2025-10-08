from dataclasses import dataclass
from dataclass_wizard import JSONWizard


@dataclass
class BacktabMember(JSONWizard):
    name: str
    id: int
    display: str
    pin: str
    # assuming only members have member definition
    is_member: bool = False
