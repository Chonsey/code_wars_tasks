


def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    if (p1, p2) == ("rock", "scissors") or (p1, p2) == ("scissors", "paper") or (p1, p2) == ("paper", "rock"):
        return "Player 1 won!"
    return "Player 2 won!"