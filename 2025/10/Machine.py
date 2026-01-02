import re


class Machine():
    def __init__(self, line: str) -> None:
        # Parse lights pattern [.##.]
        lights_match = re.search(r'\[([.#]+)\]', line)
        if lights_match is not None:
            self.target = lights_match.group(1)
        self.num_lights = len(self.target)

        # Parse buttons (x) or (x,y,z)
        buttons_matches = re.findall(r'\(([0-9,]+)\)', line)
        self.buttons = []
        for match in buttons_matches:
            indices = [int(x) for x in match.split(',')]
            self.buttons.append(indices)

        # Parse joltage {x,y,z}
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        if joltage_match is not None:
            self.joltage = [int(x) for x in joltage_match.group(1).split(',')]
        self.num_counters = len(self.joltage)

    def __repr__(self) -> str:
        return f"[{self.target}] buttons={self.buttons} joltage={self.joltage}"

    def get_target_vector(self) -> list[int]:
        """Convert target pattern to binary vector"""
        return [1 if c == '#' else 0 for c in self.target]

    def get_button_vectors(self) -> list[list[int]]:
        """Get button effects as binary vectors for lights"""
        vectors = []
        for button in self.buttons:
            vec = [0] * self.num_lights
            for idx in button:
                vec[idx] = 1
            vectors.append(vec)
        return vectors

    def get_button_counter_vectors(self) -> list[list[int]]:
        """Get button effects on counters (for part 2)"""
        vectors = []
        for button in self.buttons:
            vec = [0] * self.num_counters
            for idx in button:
                if idx < self.num_counters:
                    vec[idx] = 1
            vectors.append(vec)
        return vectors
