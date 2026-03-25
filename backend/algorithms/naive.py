import time
from base import SearchStrategy, SearchResult, SearchStep

class NaiveSearch(SearchStrategy):

    @property
    def name(self) -> str:
        return "Naive"

    @property
    def complexity(self) -> dict:
        return {
            "best":    "O(n)",
            "average": "O(n * m)",
            "worst":   "O(n * m)"
        }

    def search(self, text, pattern) -> SearchResult:
        matches = []
        comparisons = 0
        inicio = time.time()

        for i in range(len(text)):
            for j in range(len(pattern)):
                comparisons += 1   
                if text[i] != pattern[j]:
                    break
            else:
                matches.append(i)

        fim = time.time()
        tempo = (fim - inicio) * 1000

        return SearchResult(
             algorithm = self.name, 
            pattern = pattern, 
            text_length = len(text), 
            matches = matches, 
            comparisons = comparisons, 
            execution_time_ms = tempo,
            steps=[

            ] 
        )