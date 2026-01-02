class Ingredient:
    def __init__(self, line: str) -> None:
        # Parse the line
        # Example: "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8"
        parts = line.split()
        self.name: str = parts[0].rstrip(':')
        self.capacity: int = int(parts[2].rstrip(','))
        self.durability: int = int(parts[4].rstrip(','))
        self.flavor: int = int(parts[6].rstrip(','))
        self.texture: int = int(parts[8].rstrip(','))
        self.calories: int = int(parts[10])

    def __repr__(self) -> str:
        return (
            f"{self.name}: capacity {self.capacity}, "
            f"durability {self.durability}, flavor {self.flavor}, "
            f"texture {self.texture}, calories {self.calories}"
        )
