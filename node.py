ROWS = 20
COLS = 20


class Node:
    """Represents a cell/node in the grid.

    Coordinates are stored as (x, y) where x is the row index and y is the column index.
    """

    def __init__(self, x: int, y: int, walkable: bool = True):
        # x is row, y is column
        self.x: int = x
        self.y: int = y
        self.walkable: bool = walkable
        self.color = (255, 255, 255)
        self.f_score = float("inf")
        self.g_score = float("inf")
        self.h_score = float("inf")
        self.previous = None
        self.is_start = False
        self.is_end = False

    # compatibility: some modules expect .row/.col
    @property
    def row(self) -> int:
        return self.x

    @property
    def col(self) -> int:
        return self.y

    def set_start(self) -> None:
        """Mark this node as the start node."""
        self.is_start = True
        self.color = (0, 0, 255)

    def set_end(self) -> None:
        """Mark this node as the end node."""
        self.is_end = True
        self.color = (255, 165, 0)

    def __repr__(self) -> str:
        return f"Node({self.x}, {self.y})"

    def __lt__(self, other: "Node") -> bool:
        return self.f_score < other.f_score

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return False
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        # Node identity is its coordinate
        return hash((self.x, self.y))