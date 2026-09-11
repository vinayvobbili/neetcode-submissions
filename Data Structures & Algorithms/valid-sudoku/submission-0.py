class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid = True
        b = board
        row_0 = b[0]
        row_1 = b[1]
        row_2 = b[2]
        row_3 = b[3]
        row_4 = b[4]
        row_5 = b[5]
        row_6 = b[6]
        row_7 = b[7]
        row_8 = b[8]
        
        column_0 = [b[0][0], b[1][0], b[2][0], b[3][0], b[4][0], b[5][0], b[6][0], b[7][0], b[8][0]]
        column_1 = [b[0][1], b[1][1], b[2][1], b[3][1], b[4][1], b[5][1], b[6][1], b[7][1], b[8][1]]
        column_2 = [b[0][2], b[1][2], b[2][2], b[3][2], b[4][2], b[5][2], b[6][2], b[7][2], b[8][2]]
        column_3 = [b[0][3], b[1][3], b[2][3], b[3][3], b[4][3], b[5][3], b[6][3], b[7][3], b[8][3]]
        column_4 = [b[0][4], b[1][4], b[2][4], b[3][4], b[4][4], b[5][4], b[6][4], b[7][4], b[8][4]]
        column_5 = [b[0][5], b[1][5], b[2][5], b[3][5], b[4][5], b[5][5], b[6][5], b[7][5], b[8][5]]
        column_6 = [b[0][6], b[1][6], b[2][6], b[3][6], b[4][6], b[5][6], b[6][6], b[7][6], b[8][6]]
        column_7 = [b[0][7], b[1][7], b[2][7], b[3][7], b[4][7], b[5][7], b[6][7], b[7][7], b[8][7]]
        column_8 = [b[0][8], b[1][8], b[2][8], b[3][8], b[4][8], b[5][8], b[6][8], b[7][8], b[8][8]]

        sub_box_0 = [b[0][0], b[0][1], b[0][2], b[1][0], b[1][1], b[1][2], b[2][0], b[2][1], b[2][2]]
        sub_box_1 = [b[0][3], b[0][4], b[0][5], b[1][3], b[1][4], b[1][5], b[2][3], b[2][4], b[2][5]]
        sub_box_2 = [b[0][6], b[0][7], b[0][8], b[1][6], b[1][7], b[1][8], b[2][6], b[2][7], b[2][8]]

        sub_box_3 = [b[3][0], b[3][1], b[3][2], b[4][0], b[4][1], b[4][2], b[5][0], b[5][1], b[5][2]]
        sub_box_4 = [b[3][3], b[3][4], b[3][5], b[4][3], b[4][4], b[4][5], b[5][3], b[5][4], b[5][5]]
        sub_box_5 = [b[3][6], b[3][7], b[3][8], b[4][6], b[4][7], b[4][8], b[5][6], b[5][7], b[5][8]]

        sub_box_6 = [b[6][0], b[6][1], b[6][2], b[7][0], b[7][1], b[7][2], b[8][0], b[8][1], b[8][2]]
        sub_box_7 = [b[6][3], b[6][4], b[6][5], b[7][3], b[7][4], b[7][5], b[8][3], b[8][4], b[8][5]]
        sub_box_8 = [b[6][6], b[6][7], b[6][8], b[7][6], b[7][7], b[7][8], b[8][6], b[8][7], b[8][8]]

        rows = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8]
        columns = [column_0, column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8]
        sub_boxes = [sub_box_0, sub_box_1, sub_box_2, sub_box_3, sub_box_4, sub_box_5, sub_box_6, sub_box_7, sub_box_8]

        for row in rows:
            seen = {
                "1": False,
                "2": False,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": False,
                "8": False,
                "9": False,
            }
            for cell in row:
                if cell == '.':
                    continue
                if seen[cell]:
                    is_valid = False
                else:
                    seen[cell] = True
                    
        for column in columns:
            seen = {
                "1": False,
                "2": False,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": False,
                "8": False,
                "9": False,
            }
            for cell in column:
                if cell == '.':
                    continue
                if seen[cell]:
                    is_valid = False
                else:
                    seen[cell] = True

        for sub_box in sub_boxes:
            seen = {
                "1": False,
                "2": False,
                "3": False,
                "4": False,
                "5": False,
                "6": False,
                "7": False,
                "8": False,
                "9": False,
            }
            for cell in sub_box:
                if cell == '.':
                    continue
                if seen[cell]:
                    is_valid = False
                else:
                    seen[cell] = True

        return is_valid


    


        