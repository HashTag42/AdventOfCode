from IPv7Segment import IPv7Segment
import re


###############################################################################
# region Address
class IPv7Address:
    def __init__(self, address: str) -> None:
        self.address: str = address
        self.segments: list[IPv7Segment] = self._get_segments()
        self.supports_SSL: bool = self._supports_SSL()
        self.supports_TLS: bool = self._supports_TLS()

    def _get_segments(self) -> list[IPv7Segment]:
        # Split but keep the delimiters (bracketed parts)
        parts = re.split(r'(\[[a-z]+\])', self.address)
        return [IPv7Segment(part) for part in parts if part]

    def _supports_SSL(self) -> bool:
        supernet_ABAs = [
            aba for seg in self.segments if not seg.is_hypernet for aba in seg.ABAs
        ]
        hypernet_ABAs = {
            aba for seg in self.segments if seg.is_hypernet for aba in seg.ABAs
        }
        return any(aba[1] + aba[0] + aba[1] in hypernet_ABAs for aba in supernet_ABAs)

    def _supports_TLS(self) -> bool:
        has_abba_in_supernet = any(
            seg.has_ABBA for seg in self.segments if not seg.is_hypernet
        )
        has_abba_in_hypernet = any(
            seg.has_ABBA for seg in self.segments if seg.is_hypernet
        )
        return has_abba_in_supernet and not has_abba_in_hypernet

    def __repr__(self) -> str:
        return f'{self.address}, {self.supports_TLS=}, {self.supports_SSL=}'
# endregion
###############################################################################
