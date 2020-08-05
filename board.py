class Board:
    def __init__(self):
        self.board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "}

    def print_board(self):
        print(self.board["TL"] + "|" + self.board["TM"] \
            + "|" + self.board["TR"] + "|")
        print("-+" * 3)
        print(self.board["ML"] + "|" + self.board["MM"] \
            + "|" + self.board["MR"] + "|")
        print("-+" * 3)
        print(self.board["BL"] + "|" + self.board["BM"] \
            + "|" + self.board["BR"] + "|")