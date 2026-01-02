import re
from collections import Counter


class Room:
    def __init__(self, room: str) -> None:
        self.full_name: str = room
        self.encrypted_name, self.sector_id, self.checksum = self._parse_full_name()
        self.is_real: bool = self._is_real()
        self.decrypted_name: str = self._shift_str(self.encrypted_name, self.sector_id)

    def _parse_full_name(self) -> tuple[str, int, str]:
        match = re.match(r'(.+)-(\d+)\[(\w+)\]', self.full_name)
        if match:
            encrypted_name, sector_id, checksum = match.groups()
        else:
            raise ValueError(f"Invalid room: {self.full_name}")
        return encrypted_name, int(sector_id), checksum

    def _is_real(self) -> bool:
        counter = Counter(c for c in self.encrypted_name if c.isalpha())
        sorted_chars = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
        top_5 = ''.join(char for char, count in sorted_chars[:5])
        return top_5 == self.checksum

    def _shift_str(self, s: str, n: int) -> str:
        shifted = ''.join(self._shift_char(c, n) if c.isalpha() else c for c in s)
        shifted = shifted.replace('-', ' ')
        return shifted

    def _shift_char(self, c: str, n: int):
        return chr((ord(c) - ord('a') + n) % 26 + ord('a'))
