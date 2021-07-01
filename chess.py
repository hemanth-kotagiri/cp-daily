# input 1 is for white.
# input 2 is for black.
# input 3 is a sequence of valid moves.


def sol():
    scores = {
        "K": 0,
        "R": 5,
        "P": 1,
        "B": 3,
        "N": 3,
        "Q": 9,
    }
    blackPositions = {}
    whitePositions = {}
    blackScore = 0
    whiteScore = 0

    whiteString = input()
    blackString = input()

    # Step 1 : Filling up the positions and scores.
    for i in range(0, len(blackString)-2, 3):
        currentPiece = blackString[i:i+3]
        currentScore = scores[currentPiece[0]]

        blackPositions[currentPiece] = currentScore
        blackScore += currentScore

    for i in range(0, len(whiteString)-2, 3):
        currentPiece = whiteString[i:i+3]
        currentScore = scores[currentPiece[0]]

        whitePositions[currentPiece] = currentScore
        whiteScore += currentScore

    # print("Score of white: ", whiteScore)
    # print("Score of black: ", blackScore)

    # Now, third input which is a sequence of moves starting from white.
    # Captures may happen, and eliminate the pieces by mutual correspondence.
    # Assumes that all the moves are valid.
    nextMoves = input()
    whiteMove = True
    # Maybe, we don't have to store previous positions


def main():
    sol()


if __name__ == "__main__":
    main()
