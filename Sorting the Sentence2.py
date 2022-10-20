class Solution:
    def sortSentence(self, s: str) -> str:
        shuffle = s.split(" ")
        final_sen = ""

        for i in range(len(shuffle)):
            min_index = i
            for j in range(i +1, len(shuffle)):
                if shuffle[j][-1] < shuffle[min_index][-1]:
                    min_index = j

            if i != min_index:
                shuffle[min_index], shuffle[i] = shuffle[i], shuffle[min_index]
            final_sen += shuffle[i][:-1] + " "
        return (final_sen[:-1])
