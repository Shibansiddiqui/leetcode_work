class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for i in strs:
            key = "".join(sorted(i))   
            if key not in freq:
                freq[key] =[i]

            else:
                freq[key].append(i)  
         
        return list(freq.values())



        #  freq = {}

        # for key in strs:
        #     sorted_key = tuple(sorted(key))

        #     if sorted_key not in freq:
        #         freq[sorted_key] = [key]
        #     else:
        #         freq[sorted_key].append(key)

        # return list(freq.values())
            