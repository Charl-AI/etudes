local autograd = require("autograd")
local matrix = require("matrix")

local M = {}

local Linear = {}
Linear.__index = Linear

function Linear:new(in_dim, out_dim)
  local out = setmetatable({}, Linear)
  out.in_dim = in_dim
  out.out_dim = out_dim

  local weights = {}
  for i = 1, in_dim do
    weights[i] = {}
    for j = 1, out_dim do
      local w = math.random(-1, 1)
      weights[i][j] = autograd.Value:new(w)
    end
  end

  local biases = {}
  for i = 1, out_dim do
    local b = math.random(-1, 1)
    biases[i] = autograd.Value:new(b)
  end

  out.weights = matrix.Matrix:new(weights)
  out.biases = matrix.Matrix:new({ biases })
  return out
end

function Linear:forward(x)
  -- x is shape (1, in_dim),
  -- w is shape (in_dim, out_dim)
  -- b is shape (1, out_dim)
  return x * self.weights + self.biases
end

-- NB. should be called after .backward()
function Linear:sgd_update(lr)
  for i = 1, self.in_dim do
    for j = 1, self.out_dim do
      local w = self.weights.getitem({ i, j })
      w.data = w.data - lr * w.grad
    end
  end

  for i = 1, self.out_dim do
    local b = self.biases.getitem({ 1, i })
    b.data = b.data - lr * b.grad
  end
end

local function relu(x)
  assert(x.shape[1] == 1, "X must be shape (1,N)")
  local data = { {} }
  for i = 1, x.shape[2] do
    data[1][i] = x.getitem({ 1, i }):relu()
  end

  local out = matrix.Matrix(data)
  return out
end

local Mlp = {}
Mlp.__index = Mlp

function Mlp:new(in_dim, out_dim, depth, width)
  assert(depth >= 3, "Depth must be >=3")
  local layers = {}
  layers[1] = Linear:new(in_dim, width)
  for i = 2, depth - 1 do
    layers[i] = Linear:new(width, width)
  end
  layers[depth] = Linear:new(width, out_dim)

  local out = setmetatable({}, Linear)
  out.layers = layers
  return out
end

function Mlp:forward(x)
  for i = 1, self.depth - 1 do
    x = self.layers[i]:forward(x)
    x = relu(x)
  end
  return self.layers[self.depth]:forward(x)
end

function Mlp:sgd_update(lr)
  for _, layer in ipairs(self.layers) do
    layer:sgd_update(lr)
  end
end

M.Linear = Linear
M.relu = relu
M.Mlp = Mlp
return M
