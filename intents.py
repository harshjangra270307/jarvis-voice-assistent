import re

class IntentEngine:
    # Load phrase-to-intent mapping, support localization.
    def __init__(self, phrase_path='phrases/phrases.txt'):
        self.rules = []
        self.load_phrases(phrase_path)

    def load_phrases(self, path):
        with open(path, encoding='utf-8') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    intent, pattern = line.strip().split('=', 1)
                    self.rules.append((intent, re.compile(pattern, re.I)))

    def parse(self, text, lang):
        for intent, pattern in self.rules:
            if pattern.search(text):
                groups = pattern.findall(text)
                args = groups[0] if groups else []
                return intent, args if isinstance(args, list) else [args]
        return None
