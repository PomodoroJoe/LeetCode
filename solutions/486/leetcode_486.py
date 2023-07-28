#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  15.27%
# Memory:   99.76%


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        PLAYER_1 = 1
        PLAYER_2 = 2

        def PredictTheWinnerRecurse(left_index, right_index, player, relative_score):
            if left_index > right_index:
                return relative_score

            if left_index == right_index:
                if player == PLAYER_1:
                    relative_score += nums[left_index]
                else:
                    relative_score -= nums[left_index]
                return relative_score

            if player == PLAYER_1:
                #PLAYER 1
                # take left element
                new_relative_score = relative_score + nums[left_index]
                option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, PLAYER_2, new_relative_score)

                # take right element
                new_relative_score = relative_score + nums[right_index]
                option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, PLAYER_2, new_relative_score)

                return max(option_1, option_2)

            else:
                # PLAYER 2
                # take left element
                new_relative_score = relative_score - nums[left_index]
                option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, PLAYER_1, new_relative_score)

                # take right element
                new_relative_score = relative_score - nums[right_index]
                option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, PLAYER_1, new_relative_score)

                return min(option_1, option_2)

        result = PredictTheWinnerRecurse(0, len(nums) - 1, PLAYER_1, 0)
        return result >= 0



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  26.18%
# Memory:    7.88%


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        PLAYER_1 = 1
        PLAYER_2 = 2

        @cache
        def PredictTheWinnerRecurse(left_index, right_index, player, relative_score):
            if left_index > right_index:
                return relative_score

            if left_index == right_index:
                if player == PLAYER_1:
                    relative_score += nums[left_index]
                else:
                    relative_score -= nums[left_index]
                return relative_score

            if player == PLAYER_1:
                #PLAYER 1
                # take left element
                new_relative_score = relative_score + nums[left_index]
                option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, PLAYER_2, new_relative_score)

                # take right element
                new_relative_score = relative_score + nums[right_index]
                option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, PLAYER_2, new_relative_score)

                return max(option_1, option_2)

            else:
                # PLAYER 2
                # take left element
                new_relative_score = relative_score - nums[left_index]
                option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, PLAYER_1, new_relative_score)

                # take right element
                new_relative_score = relative_score - nums[right_index]
                option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, PLAYER_1, new_relative_score)

                return min(option_1, option_2)

        result = PredictTheWinnerRecurse(0, len(nums) - 1, PLAYER_1, 0)
        return result >= 0



#------------------------------------------------------
# Solution 3 - Solution 1 w/ code sharing
#------------------------------------------------------

# Runtime:  13.58%
# Memory:   43.52%


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        PLAYER_1 = 1
        PLAYER_2 = -1

        def PredictTheWinnerRecurse(left_index, right_index, player, relative_score):
            if left_index > right_index:
                return relative_score

            if left_index == right_index:
                if player == PLAYER_1:
                    relative_score += nums[left_index]
                else:
                    relative_score -= nums[left_index]
                return relative_score

            # take left element
            new_relative_score = relative_score + (nums[left_index] * player)
            option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, -player, new_relative_score)

            # take right element
            new_relative_score = relative_score + (nums[right_index] * player)
            option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, -player, new_relative_score)

            return max(option_1, option_2) if player == 1 else min(option_1, option_2)

        result = PredictTheWinnerRecurse(0, len(nums) - 1, PLAYER_1, 0)
        return result >= 0


#------------------------------------------------------
# Solution 4 - Solution 3 w/ code clean-up
#------------------------------------------------------

# Runtime:  15.30%
# Memory:   97.58%


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def PredictTheWinnerRecurse(left_index, right_index, player, relative_score):
            if left_index == right_index:
                relative_score += (nums[left_index] * player)
                return relative_score

            # take left element
            new_relative_score = relative_score + (nums[left_index] * player)
            option_1 = PredictTheWinnerRecurse(left_index + 1, right_index, -player, new_relative_score)

            # take right element
            new_relative_score = relative_score + (nums[right_index] * player)
            option_2 = PredictTheWinnerRecurse(left_index, right_index - 1, -player, new_relative_score)

            return max(option_1, option_2) if player == 1 else min(option_1, option_2)

        result = PredictTheWinnerRecurse(0, len(nums) - 1, 1, 0)
        return result >= 0