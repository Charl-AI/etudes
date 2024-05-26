INPUT_FILE = "data/2021/day02.txt"

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
	print("Loaded " .. #directions .. " instructions from " .. filename)
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

local directions, amounts = parse_file(INPUT_FILE)

print("Solution to part a:")
print(solve_part_a(directions, amounts))

print("Solution to part b:")
print(solve_part_b(directions, amounts))
