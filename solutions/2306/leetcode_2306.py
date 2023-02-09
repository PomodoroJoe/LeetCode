#------------------------------------------------------
# Solution 1 - set difference
#------------------------------------------------------

# Runtime:  72.83%
# Memory:   11.96%



class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        result = 0

        letter_to_idea_map = defaultdict(set)
        letters = set()

        for idea in ideas:
            letter = idea[0]
            letter_to_idea_map[letter].add(idea[1:])
            letters.add(letter)

        letters_list = list(letters)
        letters_count = len(letters)

        for i in range(letters_count):
            i_letter = letters_list[i]

            for j in range(i+1, letters_count):
                j_letter = letters_list[j]

                i_ideas = letter_to_idea_map[i_letter]
                j_ideas = letter_to_idea_map[j_letter]

                i_unique = i_ideas - j_ideas
                j_unique = j_ideas - i_ideas

                result += (len(i_unique) * len(j_unique)) * 2

        return result



#------------------------------------------------------
# Solution 2 - set difference w/ "optimization"
#------------------------------------------------------

# Runtime:  70.65%
# Memory:   10.87%



class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        result = 0

        letter_to_idea_map = defaultdict(set)
        letters = set()

        for idea in ideas:
            letter = idea[0]
            letter_to_idea_map[letter].add(idea[1:])
            letters.add(letter)

        letters_list = list(letters)
        letters_count = len(letters)

        for i in range(letters_count):
            i_letter = letters_list[i]
            i_ideas = letter_to_idea_map[i_letter]

            for j in range(i+1, letters_count):
                j_letter = letters_list[j]
                j_ideas = letter_to_idea_map[j_letter]

                i_unique = i_ideas - j_ideas
                j_unique = j_ideas - i_ideas

                result += (len(i_unique) * len(j_unique)) * 2

        return result