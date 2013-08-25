# TopCoder problem - Single Round Match 569 Round 1 - Division II, Level One
# Problem Name: TheJediTestDiv2
# Author's User Name: flygeneticist

# Given 1-50 floors with 0-1000 students per floor, find number of Jedi need to cover all students.
def countSupervisors (students, y, j)
  best_count = Hash.new # hash to store various possible results
  students.each do |i|
    # sets up counters to keep track of Jedi needed on a floor and overall
    floor_count = 0
    total_count = 0
    temp_students = students.map {|i| i}

    while (i - y - (floor_count*j)) > 0
      floor_count += 1
    end
    total_count += floor_count
    temp_students.delete_at(temp_students.index(i))

    # check all other floors, if any, and assign only Jedi when not on the most occupied floor.
    temp_students.each do |floor|
      floor_count = 0
      while (floor - (floor_count*j)) > 0
        floor_count += 1
      end
      total_count += floor_count
    end
    best_count[i] = total_count
  end
  return best_count.values.min
end

# Test Cases
puts countSupervisors([10], 100, 2) # => 0
puts countSupervisors([10, 15],12,5) # => 3
puts countSupervisors([0, 0, 0, 0, 0],145,21) # => 0
puts countSupervisors([11, 13, 15], 9, 5) # => 7
puts countSupervisors([4, 7, 10, 5, 6, 55, 2], 20, 3) # => 26
