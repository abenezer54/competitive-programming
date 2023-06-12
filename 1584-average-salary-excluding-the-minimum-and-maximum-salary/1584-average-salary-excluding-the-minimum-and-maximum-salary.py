class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        print(salary)
        print(sum(salary[1:len(salary) - 1]))
        return sum(salary[1:len(salary) - 1])/ (len(salary) - 2)