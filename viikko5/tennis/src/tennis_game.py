class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1


    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_even()
        elif self.player1_score >= 4 or self.player2_score >= 4:
           return self.over_four_score()

        return self.count_score()
    
    
    def count_score(self):
        player_score = 0
        score_text = ""

        number_of_players = 2

        for player in range(1, number_of_players+1):
            if player == 1:
                player_score = self.player1_score
            if player == 2:
                score_text = score_text + "-"
                player_score = self.player2_score

            if player_score == 0:
                score_text += "Love"
            elif player_score == 1:
                score_text += "Fifteen"
            elif player_score == 2:
                score_text += "Thirty"
            elif player_score == 3:
                score_text += "Forty"
        
        return score_text


    def score_even(self):
        score_text = ""

        if self.player1_score == 0:
            score_text = "Love-All"
        elif self.player1_score == 1:
            score_text = "Fifteen-All"
        elif self.player1_score == 2:
            score_text = "Thirty-All"
        elif self.player1_score == 3:
            score_text = "Forty-All"
        else:
            score_text = "Deuce"
        
        return score_text
    
    
    def over_four_score(self):
        score_text = ""
        advantage = self.player1_score - self. player2_score

        if advantage == 1:
            score_text = "Advantage player1"
        elif advantage == -1:
            score_text = "Advantage player2"
        elif advantage >= 2:
            score_text = "Win for player1"
        else:
            score_text = "Win for player2"
        
        return score_text