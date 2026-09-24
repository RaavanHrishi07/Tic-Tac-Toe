class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current_player = "X"

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

    def show_positions(self):
        print("\nBoard positions:")
        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")
        print()

    def make_move(self, position):
        index = position - 1

        if self.board[index] != " ":
            return False

        self.board[index] = self.current_player
        return True

    def check_winner(self):
        winning_patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for first, second, third in winning_patterns:
            if (
                self.board[first] != " "
                and self.board[first] == self.board[second]
                and self.board[second] == self.board[third]
            ):
                return self.board[first]

        return None

    def board_full(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        print("\n===== TIC TAC TOE =====")
        self.show_positions()

        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn.")

            try:
                position = int(input("Choose a position (1-9): "))

                if position < 1 or position > 9:
                    print("Please choose a number between 1 and 9.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if not self.make_move(position):
                print("That position is already occupied. Choose another one.")
                continue

            winner = self.check_winner()

            if winner:
                self.display_board()
                print(f"🎉 Player {winner} wins!")
                break

            if self.board_full():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()


def main():
    while True:
        game = TicTacToe()
        game.play()

        again = input("\nPlay again? (y/n): ").strip().lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()