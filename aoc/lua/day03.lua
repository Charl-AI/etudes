INPUT_FILE = "data/2021/day03.txt"

-- parse file into a matrix
local function parse_file(filepath)
  local matrix = {}

  for line in io.lines(filepath) do
    local row = {}
    -- each row is a series of binary numbers e.g. "00111011"
    for c in string.gmatch(line, "%d") do
      table.insert(row, tonumber(c))
    end
    table.insert(matrix, row)
  end

  print("Loaded " .. #matrix .. " rows from " .. filepath)
  return matrix
end

local function solve_part_a(matrix)
  local gamma = "" -- composed of most common bit in each column
  local epsilon = "" -- composed of least common bit in each column

  for j = 1, #matrix[1] do
    local ones = 0
    local zeros = 0
    for i = 1, #matrix do
      if matrix[i][j] == 1 then
        ones = ones + 1
      else
        zeros = zeros + 1
      end
    end
    if ones > zeros then
      gamma = gamma .. "1"
      epsilon = epsilon .. "0"
    else
      gamma = gamma .. "0"
      epsilon = epsilon .. "1"
    end
  end

  return tonumber(gamma, 2) * tonumber(epsilon, 2)
end

local function solve_part_b(matrix)
  local oxygen = "" --
  local scrubber = ""

  return tonumber(oxygen, 2) * tonumber(scrubber, 2)
end

local matrix = parse_file(INPUT_FILE)

print("Solution to part a:")
print(solve_part_a(matrix))

print("Solution to part b:")
print("Part B not implemented yet.")
