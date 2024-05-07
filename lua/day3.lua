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

local question, filepath = parse_args()
local matrix = parse_file(filepath)

if question == "a" then
	print(solve_part_a(matrix))
else
	print("Part B not implemented yet.")
end
