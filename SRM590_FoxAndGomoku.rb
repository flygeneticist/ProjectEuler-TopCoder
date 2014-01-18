# TopCoder problem - Single Round Match 590 Round 1 - Division II, Level One
# Problem Name: FoxAndGomoku
# Author's User Name: flygeneticist

#You are given a String[] board that represents a square board.
#The character board[i][j] represents the cell with coordinates (i,j).
#Each of those characters is either '.' (representing an empty cell) or 'o' (representing a cell with a piece).
#Determine whether there are 5 consecutive cells (horizontally, vertically, or diagonally) that contain Jiro's tokens.
#Return "found" (quotes for clarity) if there are five such cells anywhere on the board. Otherwise, return "not found".

def consecutive (board)
  puts
  puts "~~~ NEW PUZZLE ~~~"

  # setup variables needed
  consecutive_zeros = 0
  current_row = -1

  # work through board rows to find consecutive cells horizontally
  # if first cell in a row <> 'o', jump 4 cells forward for next cell to search
  for row in (0..(board.length-1)) do
    consecutive_zeros = 0
    for cell in (0..(board[0].length-1))
      if board[row][cell] == "o"
        consecutive_zeros += 1
        if consecutive_zeros == 5
          return "found horizontally"
        end
      else
        consecutive_zeros = 0
      end
    end
  end

  # work through board rows to find consecutive cells vertically
  for cell in (0..(board[0].length-1)) do
    consecutive_zeros = 0
    for row in (0..(board.length-1))
      if board[row][cell] == "o"
        consecutive_zeros += 1
        if consecutive_zeros == 5
          return "found vertically"
        end
      else
        consecutive_zeros = 0
      end
    end
  end
  puts "not found"

   # work through board rows to find consecutive cells diagonally
   # consider the length of a row and the num of rows remaining to determine if possible

end


def search_params(board, current_row, current_cell)
  # define cell positions surrounding the current cell
  investigate_row = current_row + 1

  if (current_cell + 1) >= board[0].length
    # No more cells to the right to search!
    r_cell = 0
    br_cell = 0
  else
    # set all right cells
    r_cell = [current_row, (current_cell + 1)]
    br_cell = [investigate_row, (current_cell + 1)]
  end

  if (current_cell - 1) == -1
    # No more cells to the left to search!
    bl_cell = 0
  else
    # set bottom-left cells
    bl_cell = [investigate_row, (current_cell - 1)]
  end

  if investigate_row >= board.length
    # at the end of the board. No more rows to search!
    bl_cell = 0
    b_cell = 0
    br_cell = 0
  else
    b_cell = [investigate_row, current_cell]
  end

  surrounding_cells = [r_cell, bl_cell, b_cell, br_cell]
  return surrounding_cells
end

def search_surroundings (surrounding_cells)
  # check the surrounding cells for zeros if search_param is valid (ie. not beyond edges of board)
end
