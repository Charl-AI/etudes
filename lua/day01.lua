INPUT_FILE = "data/2021/day01.txt"

local function solve_part_a(m)
	local num_increases = 0
	for i = 2, #m do
		if m[i] > m[i - 1] then
			num_increases = num_increases + 1
		end
	end
	return num_increases
end

-- the trick here is that to check if the sum of a sliding window increases,
-- we only need to check if the number coming in is greater than the number
-- going out.
local function solve_part_b(m)
	local num_increases = 0
	for i = 4, #m do
		if m[i] > m[i - 3] then
			num_increases = num_increases + 1
		end
	end
	return num_increases
end

-- measurements are lines in the input file
-- here we read into a table/list
local measurements = {}

for line in io.lines(INPUT_FILE) do
	table.insert(measurements, tonumber(line))
end

print("Loaded " .. #measurements .. " measurements from " .. INPUT_FILE)

print("Solution to part a:")
print(solve_part_a(measurements))

print("Solution to part b:")
print(solve_part_b(measurements))
