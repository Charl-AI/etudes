-- A very simple 2D matrix in pure lua

local M = {}

local Matrix = {}
Matrix.__index = Matrix

-- construct matrix from nested tables
-- each element of the matrix can be a number or autograd.Value
function Matrix:new(data)
  local out = setmetatable({}, Matrix)

  local dim1 = #data
  local dim2 = #data[1]
  for _, row in ipairs(data) do
    assert(#row == dim2, "All rows must be uniform length.")
  end

  out.data = data
  out.transposed = false
  out.shape = { dim1, dim2 }
  return out
end

function Matrix:__eq(other)
  if self.shape[0] ~= other.shape[0] or self.shape[1] ~= other.shape[1] then
    return false
  end

  for i = 1, self.shape[1] do
    for j = 1, self.shape[2] do
      if self:getitem({ i, j }) ~= other:getitem({ i, j }) then
        return false
      end
    end
  end
  return true
end

function Matrix:transpose()
  -- transposing doesn't affect memory layout,
  -- it just sets a flag to change how the getters
  -- and setters are interpreted
  self.shape = { self.shape[2], self.shape[1] }
  if self.transposed == false then
    self.transposed = true
  else
    self.transposed = false
  end
end

function Matrix:repr()
  local result = "Shape:" .. table.concat(self.shape, ", ")
  result = result .. "\nData:\n"

  for i = 1, self.shape[1] do
    result = result .. "{ "
    for j = 1, self.shape[2] do
      local item = self:getitem({ i, j })
      local str = "N/A"
      if type(item) == "number" then
        str = item
      else
        str = item:repr()
      end
      result = result .. str .. " "
    end
    result = result .. "}\n"
  end

  return result
end

function Matrix:getitem(idxs)
  if self.transposed == true then
    idxs = { idxs[2], idxs[1] } -- flip indices if transposed
  end
  return self.data[idxs[1]][idxs[2]]
end

function Matrix:setitem(idxs, item)
  if self.transposed == true then
    idxs = { idxs[2], idxs[1] } -- flip indices if transposed
  end
  self.data[idxs[1]][idxs[2]] = item
end

function Matrix:__add(other)
  assert(self.shape[1] == other.shape[1], "Cannot add matrices with different shapes.")
  assert(self.shape[2] == other.shape[2], "Cannot add matrices with different shapes.")
  local data = {}
  for i = 1, self.shape[1] do
    data[i] = {}
    for j = 1, self.shape[2] do
      data[i][j] = self:getitem({ i, j }) + other:getitem({ i, j })
    end
  end

  local out = Matrix:new(data)
  return out
end

function Matrix:__mul(other)
  assert(self.shape[2] == other.shape[1], "Cannot multiply matrices without matching inner dim.")
  local output_shape = { self.shape[1], other.shape[2] }
  local data = {}
  for i = 1, output_shape[1] do
    data[i] = {}
    for j = 1, output_shape[2] do
      local sum = 0
      for k = 1, self.shape[2] do
        sum = sum + self:getitem({ i, k }) * other:getitem({ k, j })
      end
      data[i][j] = sum
    end
  end

  local out = Matrix:new(data)
  return out
end

M.Matrix = Matrix
return M
