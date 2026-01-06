###############################################################################
# region Segment
class IPv7Segment:
    def __init__(self, segment: str) -> None:
        if segment.startswith('['):
            self.segment = segment[1:-1]
            self.is_hypernet = True
        else:
            self.segment = segment
            self.is_hypernet = False
        self.has_ABBA: bool = self._has_ABBA()
        self.ABAs: list[str] = self._get_ABAs()

    def _get_ABAs(self) -> list[str]:
        length = len(self.segment)
        if length < 3:
            return []
        return [
            self.segment[i:i + 3]
            for i in range(length - 2)
            if self._is_ABA(self.segment[i:i + 3])
        ]

    def _has_ABBA(self) -> bool:
        length = len(self.segment)
        if length < 4:
            return False
        return any(
            self._is_ABBA(self.segment[i:i + 4])
            for i in range(length - 3)
        )

    def _is_ABA(self, s: str) -> bool:
        return s[0] == s[2] and s[0] != s[1]

    def _is_ABBA(self, s: str) -> bool:
        return s[0] != s[1] and s == s[::-1]

    def __repr__(self) -> str:
        return f'{self.segment}, {self.is_hypernet=}, {self.has_ABBA=}'
# endregion
###############################################################################
