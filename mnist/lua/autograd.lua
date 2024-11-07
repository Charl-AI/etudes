--[[ A pure lua autograd engine.

  This is a torch-style system, meaning that each time
  a calulation is performed, it has the side effect of building
  a computational graph. You call .backward() on the final
  output, then can inspect the .grad attribute of each input
  to get the gradient of the output wrt that input.

  y = f(a,b) forms the graph a -> y <- b, after calling y.backward():
    y.grad = 1, derivative of y wrt itself must be 1
    a.grad = df/da (a,b), partial derivative wrt a, evaluated at a,b
    b.grad = df/db (a,b), partial derivative wrt b, evaluated at a,b

  Inspired by micrograd:
  https://github.com/karpathy/micrograd.

--]]

local M = {}

local Value = {}
Value.__index = Value

function Value:new(data)
  local out = setmetatable({}, Value)

  out.data = data
  out.grad = 0
  out._parents = {}
  out._backward = function() end

  return out
end

function Value:__eq(other)
  return self.data == other.data
end

function Value:repr()
  return string.format("(Value) Data: %f, Grad: %f", self.data, self.grad)
end

function Value:backward()
  local topo = {}
  local visited = {}

  local function build_topo(v)
    if not visited[v] then
      visited[v] = true
      for _, parent in ipairs(v._parents) do
        build_topo(parent)
      end
      table.insert(topo, v)
    end
  end

  build_topo(self)
  self.grad = 1
  for i = #topo, 1, -1 do
    topo[i]._backward()
  end
end

function Value:relu()
  local data = math.max(0, self.data)
  local out = Value:new(data)
  table.insert(out._parents, self)

  local function _backward()
    if out.data > 0 then
      self.grad = self.grad + out.grad
    end
  end

  out._backward = _backward
  return out
end

function Value:__add(other)
  local data = self.data + other.data
  local out = Value:new(data)
  table.insert(out._parents, self)
  table.insert(out._parents, other)

  local function _backward()
    self.grad = self.grad + out.grad
    other.grad = other.grad + out.grad
  end

  out._backward = _backward
  return out
end

function Value:__mul(other)
  local data = self.data * other.data
  local out = Value:new(data)
  table.insert(out._parents, self)
  table.insert(out._parents, other)

  local function _backward()
    self.grad = other.data * out.grad
    other.grad = self.data * out.grad
  end

  out._backward = _backward
  return out
end

M.Value = Value
return M
