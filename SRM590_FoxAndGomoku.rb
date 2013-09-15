# TopCoder problem - Single Round Match 590 Round 1 - Division II, Level One
# Problem Name: FoxAndGomoku
# Author's User Name: flygeneticist

#You are given a String[] board that represents a square board. The character board[i][j] represents the cell with coordinates (i,j). Each of those characters is either '.' (representing an empty cell) or 'o' (representing a cell with Jiro's piece). Determine whether there are 5 consecutive cells (horizontally, vertically, or diagonally) that contain Jiro's tokens. Return "found" (quotes for clarity) if there are five such cells anywhere on the board. Otherwise, return "not found".

def consecutive (board)
  consecutive_zeros = []
  puts board
  board.each do |row|
    row = row.scan(/./)
    print row
    row.each do |cell|
      if cell == "o"
        consecutive_zeros << [board.index(row),row.index(cell)]
        # check the surrounding cells for zeros
      end
    end
  end
end

# Test Cases
consecutive([".....", ".....", ".....", ".....", "....."]) # => not found
consecutive(["ooooo", "ooooo", "ooooo", "ooooo", "ooooo"]) # => found
#consecutive(["....o.", "...o..", "..o...", ".o....", "o.....", "......"]) # => found
#consecutive(["oooo.", ".oooo", "oooo.", ".oooo", "....."]) # => not found
#consecutive(["oooo.", ".oooo", "oooo.", ".oooo", "....o"]) # => found
#consecutive(["o....", "o.o..", "o.o.o", "o.o..", "o...."]) # => found
#consecutive(["..........", "..........", "..oooooo..", "..o.......", "..o.......", "..oooooo..", ".......o..", ".......o..", "..oooooo..", ".........."]) # => found
#consecutive(["..........", "..........", "..oooo.o..", "..o.......", "..o.......", "..o.oooo..", ".......o..", ".......o..", "..oooo.o..", ".........."]) # => not found
