-- A very simple 2D matrix in pure lua

local autograd = require("autograd")

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

-- convert a matrix of number elements to a matrix of autograd.Value elements
function Matrix:attach()
  local data = {}
  for i = 1, self.shape[1] do
    data[i] = {}
    for j = 1, self.shape[2] do
      local item = self:getitem({ i, j })
      assert(type(item) == "number", "Can only attach a matrix of numbers")
      data[i][j] = autograd.Value:new(item)
    end
  end
  return Matrix:new(data)
end

-- convert a matrix of autograd.Value elements to a matrix of number elements
function Matrix:detach()
  local data = {}
  for i = 1, self.shape[1] do
    data[i] = {}
    for j = 1, self.shape[2] do
      local item = self:getitem({ i, j })
      assert(type(item) == "table", "Can only detach a matrix of autograd.Values")
      data[i][j] = item.data
    end
  end
  return Matrix:new(data)
end

function Matrix:transpose()
  local new_shape = { self.shape[2], self.shape[1] }
  local data = {}
  for i = 1, new_shape[1] do
    data[i] = {}
  end

  for i = 1, self.shape[1] do
    for j = 1, self.shape[2] do
      data[j][i] = self:getitem({ i, j })
    end
  end

  local out = Matrix:new(data)
  return out
end

function Matrix:repr()
  local result = "(Matrix) Shape: (" .. table.concat(self.shape, ", ")
  result = result .. "), Data:\n"

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
      result = result .. str .. ", "
    end
    result = result .. "}\n"
  end

  return result
end

function Matrix:getitem(idxs)
  assert(idxs[1] >= 1, "Index must be >= 1.")
  assert(idxs[2] >= 1, "Index must be >= 1.")
  assert(idxs[1] <= self.shape[1], "Attempted to index out of bounds.")
  assert(idxs[2] <= self.shape[2], "Attempted to index out of bounds.")
  return self.data[idxs[1]][idxs[2]]
end

function Matrix:setitem(idxs, item)
  assert(idxs[1] >= 1, "Index must be >= 1.")
  assert(idxs[2] >= 1, "Index must be >= 1.")
  assert(idxs[1] <= self.shape[1], "Attempted to index out of bounds.")
  assert(idxs[2] <= self.shape[2], "Attempted to index out of bounds.")
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
      data[i][j] = self:getitem({ i, 1 }) * other:getitem({ 1, j })
      for k = 2, self.shape[2] do
        data[i][j] = data[i][j] + self:getitem({ i, k }) * other:getitem({ k, j })
      end
    end
  end

  local out = Matrix:new(data)
  return out
end

M.Matrix = Matrix
return M
