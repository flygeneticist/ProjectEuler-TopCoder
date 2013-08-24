# TopCoder problem - Single Round Match 569 Round 1 - Division II, Level One
# Problem Name: TheJediTestDiv2
# Author's User Name: flygeneticist

# Given 1-50 floors with 0-1000 students per floor, find number of Jedi need to cover all students.
def countSupervisors (students, y, j)
  # sets up counters to keep track of Jedi need on a floor and overall
  sorted_students = students.sort
  levels = students.size
  total_count = 0
  floor_count = 0

  # find the floor with highest number of students
  largest_group = sorted_students.max

  # set Yoda to cover the floor with most students and check if more Jedis are needed
  while (largest_group - y - (floor_count*j)) > 0
    floor_count += 1
  end
  total_count += floor_count
  sorted_students.pop

  # check all other floors, if any, and assign only Jedi when not on the most occupied floor.
  sorted_students.each do |floor|
    floor_count = 0
    while (floor - (floor_count*j)) > 0
      floor_count += 1
    end
    total_count += floor_count
  end

  return total_count
end

puts countSupervisors([10,1000], 101, 100)
