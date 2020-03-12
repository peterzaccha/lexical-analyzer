import re
from rules import RULES
from token import Token


class Analyzer:
    def __init__(self):
        self.REGEX = re.compile(
            "|".join(self.appendGroups())
        )

    def compile(self, input):
        tokens = []
        for match in self.REGEX.finditer(input):
            if match.lastgroup == "MISMATCH":
                raise RuntimeError("Cannot recognize {}".format(match.group()))
            elif match.lastgroup == "SKIP":
                continue
            tokens.append(Token(match.lastgroup, match.group()))

        return tokens

    @staticmethod
    def appendGroups():
        newRules = []
        for type, regex, before, after in RULES:
            tokenRegex = "(?P<{}>{})".format(type, regex)
            if before is not None:
                tokenRegex = before + tokenRegex
            if after is not None:
                tokenRegex += after
            newRules.append(tokenRegex)
        return newRules
