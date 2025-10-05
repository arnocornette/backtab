import json

from backtab.members.member import BacktabMember


class BacktabMembersLoader:
    @staticmethod
    def load_from_json(raw_json_str: str):
        loaded_json = json.loads(raw_json_str)  # pyright: ignore[reportAny] cannot get type from this
        return BacktabMember(**loaded_json)  # pyright: ignore[reportAny]
