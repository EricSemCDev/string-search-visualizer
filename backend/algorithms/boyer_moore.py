from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

@dataclass
class SearchStep:
    text_index: int
    pattern_index: int
    comparison: str
    match: bool
    note: str = ""

@dataclass
class SearchResult:
    algorithm: str
    pattern: str
    text_length: int
    matches: List[int]
    comparisons: int
    execution_time_ms: float
    steps: List[SearchStep]


class SearchStrategy(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def complexity(self) -> dict:
        pass

    @abstractmethod
    def search(self, text: str, pattern: str) -> SearchResult:
        pass