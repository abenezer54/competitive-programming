class Solution:
    def interpret(self, command: str) -> str:
        c = command.replace("()", "o")
        return c.replace("(al)", "al")
        