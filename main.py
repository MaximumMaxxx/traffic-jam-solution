import math
def main():
    count = int(input("How many players? "))
    gameboard = []
    placed = 0

    switched = False
    for _ in range(count+1):
        if placed < (count/2) and switched is False:
            gameboard.append(">")
        elif placed >= (count/2) and switched is False:
            gameboard.append(" ")
            switched = True
        else:
            gameboard.append("<")
        placed += 1

    print_board(gameboard)

    print(f"Teams sizes: {gameboard.count('>')} vs {gameboard.count('<')}")

    dir = "l"
    prevspace = find_space(gameboard)
    with open(f"{count}.txt", "w") as f:
        f.write("".join(gameboard) + "\n")
        while not is_done(gameboard):
            if (is_conflict(gameboard)):
                if dir == "l":
                    # Step
                    gameboard[prevspace] = ">"
                    gameboard[prevspace-1] = " "
                    dir = "r"
                else:
                    # Step
                    gameboard[prevspace] = "<"
                    gameboard[prevspace+1] = " "
                    dir = "l"
            else:
                # Jump
                try:
                    jumpindex = findPieceThatCanJump(gameboard)
                except:
                    # Step
                    gameboard = stepFirstPiece(gameboard)

                else:
                    gameboard[prevspace] = gameboard[jumpindex]
                    gameboard[jumpindex] = " "

            prevspace = find_space(gameboard)
            print_board(gameboard)
            f.write("".join(gameboard) + "\n")
    print("Done!")


def print_board(gameboard):
    print("".join(gameboard))


def find_space(gameboard):
    return gameboard.index(" ")


def is_done(gameboard):
    dir = "<"
    for i in gameboard:
        if i == " ":
            dir = ">"
        elif i != dir:
            return False

    return True


def is_conflict(gameboard):
    spaceIndex = find_space(gameboard)
    if (gameboard[spaceIndex-1] == ">" and gameboard[spaceIndex+1] == "<") and (spaceIndex != 0 and spaceIndex != len(gameboard)-1):
        return True
    return False


def findPieceThatCanJump(gameboard):
    spaceIndex = find_space(gameboard)
    # Find the index of the piece that can jump
    for pi, piece in enumerate(gameboard):
        if piece == ">" and pi == spaceIndex - 2 and gameboard[spaceIndex-1] != ">":
            return pi
        elif piece == "<" and pi == spaceIndex + 2 and gameboard[spaceIndex+1] != "<":
            return pi
    raise Exception("No piece can jump, something went wrong with the logic")


def stepFirstPiece(gameboard):
    spaceIndex = find_space(gameboard)
    if gameboard[spaceIndex-1] == ">" and spaceIndex != 0:
        gameboard[spaceIndex] = ">"
        gameboard[spaceIndex-1] = " "
    elif gameboard[spaceIndex+1] == "<" and spaceIndex != len(gameboard)-1:
        gameboard[spaceIndex] = "<"
        gameboard[spaceIndex+1] = " "
    return gameboard


if __name__ == "__main__":
    main()
