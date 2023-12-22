class Robot:
    def operation(self, face, pos):
        if face == "North":
            pos[1] += 1
        elif face == "East":
            pos[0] += 1
        elif face == "South":
            pos[1] -= 1
        else:
            pos[0] -= 1

    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height
        self.faces = ["East", "North","West", "South"]       
        self.current_face = 0
        self.position = [0, 0]

    def step(self, num: int) -> None:
        perimeter = ((self.width + self.height) * 2 ) - 4 
        num %=  perimeter
        if num == 0:
            num = perimeter
        for i in range(num):
            prev = self.position.copy()
            self.operation(self.faces[self.current_face % 4], self.position)
            if self.position[0] > self.width - 1 or self.position[0] < 0 or self.position[1] > self.height - 1 or self.position[1] < 0:
                self.position = prev
                self.current_face += 1
                self.operation(self.faces[self.current_face % 4], self.position)

    def getPos(self) -> List[int]:
        return self.position 

    def getDir(self) -> str:
        return self.faces[self.current_face % 4]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()