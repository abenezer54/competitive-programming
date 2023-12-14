class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if (tokenId in self.tokens) and (self.tokens[tokenId] + self.time > currentTime):
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, lastTime in self.tokens.items():
            if lastTime + self.time > currentTime:
                count += 1
        return count

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)