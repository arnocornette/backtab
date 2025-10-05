import json

from backtab.products.product import BacktabProduct


class BacktabProductsLoader:
    @staticmethod
    def load_from_json(raw_json_str: str):
        loaded_json = json.loads(raw_json_str)  # pyright: ignore[reportAny] cannot get type from this
        return BacktabProduct(**loaded_json)  # pyright: ignore[reportAny]
