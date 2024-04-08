class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        i = 0
        while i < len(students) and cnt[sandwiches[i]]:
            cnt[sandwiches[i]] -= 1
            i += 1
        return len(students) - i
