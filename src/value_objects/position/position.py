from shield.guard import Guard

class Position:

    COLUMN_MAP = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
    def __init__(self, col_letter:str, row_number:int):
        Guard.againstNull(col_letter, "Column Letter") #for checkiong if the column letter in position is not null
        Guard.againstNull(row_number, "Row Number") #for checkiong if the row number in position is not null

        # for correctly standerdizing the value ... 
        col_letter = col_letter.upper()

        #checking if the the letter exits in COLUMN_MAP
        if col_letter not in self.COLUMN_MAP:
            raise Exception (f" {col_letter} is not a valid cordinate (A-H)")
        Guard.againstOutOfRange(0, 7, row_number, "Row")

        #saving the values privatly
        self._col = self.COLUMN_MAP[col_letter]
        self._row = row_number

    @property
    def col (self)->int:
        return self._col
    @property
    def row (self)->int:
        return self._row
    
    def __repr__(self) -> str:
        letter = "ABCDEFGH"
        return(f"{letter[self._col][self._row]}")

