local function parse_args()
	local question = arg[1]
	local filepath = arg[2]

	if question == nil or (question ~= "a" and question ~= "b") then
		print("Invalid question. The first CLI argument must be either 'a' or 'b'.")
		os.exit(1)
	end

	if filepath == nil then
		print("Invalid filepath. The second CLI argument must be a valid filepath.")
		os.exit(1)
	end

	return question, filepath
end

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

local question, filepath = parse_args()

-- measurements are lines in the input file
-- here we read into a table/list
local measurements = {}

for line in io.lines(filepath) do
	table.insert(measurements, tonumber(line))
end

print("Loaded " .. #measurements .. " measurements from " .. filepath)

if question == "a" then
	print(solve_part_a(measurements))
else
	print(solve_part_b(measurements))
end
