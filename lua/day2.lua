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

local function parse_file(filename)
	local directions = {} -- either up, forward, down
	local amounts = {} -- positive number

	for line in io.lines(filename) do
		-- each line has format "direction N"
		-- this is super ugly but I don't know lua very well
		local word_idx = 1
		for word in string.gmatch(line, "%S+") do
			if word_idx == 1 then
				Dir = word
			else
				N = word
			end
			word_idx = word_idx + 1
		end

		table.insert(directions, Dir)
		table.insert(amounts, tonumber(N))
	end
	print("Loaded " .. #directions .. " instructions from " .. arg[2])
	return directions, amounts
end

local function solve_part_a(directions, amounts)
	local x = 0 -- horizontal position
	local z = 0 -- depth (increases downwards)

	for i = 1, #directions do
		local dir = directions[i]
		local n = amounts[i]

		if dir == "forward" then
			x = x + n
		elseif dir == "up" then
			z = z - n
		elseif dir == "down" then
			z = z + n
		end
	end

	return x * z
end

local function solve_part_b(directions, amounts)
	local x = 0 -- horizontal position
	local z = 0 -- depth (increases downwards)
	local a = 0

	for i = 1, #directions do
		local dir = directions[i]
		local n = amounts[i]

		if dir == "forward" then
			x = x + n
			z = z + a * n
		elseif dir == "up" then
			a = a - n
		elseif dir == "down" then
			a = a + n
		end
	end

	return x * z
end

local question, filepath = parse_args()
local directions, amounts = parse_file(filepath)

if question == "a" then
	print(solve_part_a(directions, amounts))
else
	print(solve_part_b(directions, amounts))
end
