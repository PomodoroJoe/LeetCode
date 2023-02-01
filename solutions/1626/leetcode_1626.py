#------------------------------------------------------
# Solution 1 - dynamic programming
#------------------------------------------------------

# Runtime:  73.43%
# Memory:   23.80%



class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #
        #                    | SCORE
        #             1      |       2
        #                    |
        #   AGE -------------+--------------->
        #                    |
        #             4      |       3
        #                    |
        
        AGE = 0
        SCORE = 1

        players = []
        for i in range(len(scores)):
            player = (ages[i], scores[i])
            players.append(player)

        sorted_players = sorted(players, key = lambda x: (x[SCORE], x[AGE]))


        result = 0

        best_team_score_for_player = [0] * len(sorted_players)

        for i, player in enumerate(sorted_players):
            best_team_score = 0

            for j in range(i):
                teammate = sorted_players[j]
                if teammate[AGE] > player[AGE]:
                    continue

                best_team_score = max(best_team_score, best_team_score_for_player[j])

            best_team_score_for_player[i] = player[SCORE] + best_team_score

        result = max(best_team_score_for_player)
        return result