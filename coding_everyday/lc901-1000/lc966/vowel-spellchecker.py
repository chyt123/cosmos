class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        n = len(wordlist)
        m = len(queries)
        exact_set = set(wordlist)

        cap_dict = defaultdict(list)
        vowel_dict = defaultdict(list)
        for w in wordlist:
            cap_dict[w.lower()].append(w)
            vowel_dict[re.sub(r'[aeiou]', '-', w.lower())].append(w)

        # print(exact_set, cap_dict,vowel_dict)

        res = []
        for i in queries:
            i_rep = re.sub(r'[aeiou]', '-', i.lower())
            if i in exact_set:
                res.append(i)
            elif i.lower() in cap_dict:
                res.append(cap_dict[i.lower()][0])
            elif i_rep in vowel_dict:
                res.append(vowel_dict[i_rep][0])
            else:
                res.append("")
        return res