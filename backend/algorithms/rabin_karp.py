import time
from base import SearchStrategy, SearchResult, SearchStep

class RabinKarpSearch(SearchStrategy):

    @property
    def name(self) -> str:
        return "Rabin-Karp"

    @property
    def complexity(self) -> dict:
        return {
            "best/average": "O(n + m)",
            "worst":        "O(n * m)"
        }

    def search(self, text, pattern) -> SearchResult:
        BASE = 101
        PRIMO = 10**9 + 9

        m = len(pattern)
        n = len(text)

        hash_pattern = 0
        hash_window = 0

        matches = []
        comparisons = 0
        inicio = time.time()

        for i in range(m):
            hash_pattern = (hash_pattern * BASE + ord(pattern[i])) % PRIMO
            hash_window = (hash_window * BASE + ord(text[i])) % PRIMO

        for i in range(n - m + 1):
            if hash_window == hash_pattern:
                for j in range(m):
                    if text[j + i] != pattern[j]:
                        break
                else:
                    matches.append(i)
            if i < n - m:
                hash_window = (hash_window - ord(text[i]) * pow(BASE, m - 1, PRIMO)) % PRIMO
                hash_window = (hash_window * BASE + ord(text[i + m])) % PRIMO
                hash_window = (hash_window + PRIMO) % PRIMO

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