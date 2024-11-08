local autograd = require("autograd")
local matrix = require("matrix")
local nn = require("nn")

local function expect(expected, actual, msg)
  local message = msg .. "\n"
  message = message .. string.format("Expected %s, got %s", tostring(expected), tostring(actual))
  assert(expected == actual, message)
end

local function test_equality()
  local x = autograd.Value:new(1)
  local y = autograd.Value:new(1)
  local z = autograd.Value:new(2)

  expect(true, x == y, "equality of Value")
  expect(true, x ~= z, "inequality of Value")
end

test_equality()

local function test_relu()
  local x1 = autograd.Value:new(5)
  local y1 = x1:relu()

  local x2 = autograd.Value:new(-2)
  local y2 = x2:relu()

  expect(0, x1.grad, "gradient before backward pass")

  y1:backward()
  y2:backward()

  expect(5, y1.data, "relu(5)")
  expect(0, y2.data, "relu(-2)")
  expect(1, x1.grad, "grad(relu(5)) wrt input")
  expect(0, x2.grad, "grad(relu(-2)) wrt input")

  -- grad of output wrt itself is always 1
  expect(1, y1.grad, "grad(relu(5)) wrt output")
  expect(1, y2.grad, "grad(relu(5)) wrt output")
end

test_relu()

local function test_add()
  local x1 = autograd.Value:new(5)
  local x2 = autograd.Value:new(2)

  local y = x1 + x2
  y:backward()

  expect(7, y.data, "5+2")
  expect(1, x1.grad, "grad(5+2) wrt first arg")
  expect(1, x2.grad, "grad(5+2) wrt second arg")
  expect(1, y.grad, "grad(5+2) wrt output")
end

test_add()

local function test_mul()
  local x1 = autograd.Value:new(4)
  local x2 = autograd.Value:new(3)

  local y = x1 * x2
  y:backward()

  expect(12, y.data, "4*3")
  expect(3, x1.grad, "grad(4*3) wrt first arg")
  expect(4, x2.grad, "grad(4*3) wrt second arg")
  expect(1, y.grad, "grad(4*3) wrt output")
end

test_mul()

local function test_matrix_attach_detach()
  local x = matrix.Matrix:new({ { 1, 2 } })
  local y = matrix.Matrix:new({ { autograd.Value:new(1), autograd.Value:new(2) } })

  expect(y, x:attach(), "attaching matrix to graph")
  expect(x, y:detach(), "detaching matrix from graph")
  expect(x, x:attach():detach(), "attach-detach round-trip")
  expect(y, y:detach():attach(), "detach-attach round-trip")
end

test_matrix_attach_detach()

local function test_matrix_equality()
  local x = matrix.Matrix:new({ { 1, 2 }, { 3, 4 } })
  local y = matrix.Matrix:new({ { 1, 2 }, { 3, 4 } })
  local z1 = matrix.Matrix:new({ { 1, 2 }, { 3, 5 } })
  local z2 = matrix.Matrix:new({ { 1, 2 } })

  expect(true, x == y, "matrix equality")
  expect(true, x ~= z1, "matrix inequality")
  expect(true, x ~= z2, "matrix inequality")
end

test_matrix_equality()

local function test_matrix_transpose()
  local x = matrix.Matrix:new({ { 1, 2 }, { 3, 4 }, { 5, 6 } }) -- shape (3,2)

  expect(x.shape[1], x:transpose().shape[2], "shape of transposed matrix")
  expect(x.shape[2], x:transpose().shape[1], "shape of transposed matrix")
  expect(x:getitem({ 1, 2 }), x:transpose():getitem({ 2, 1 }), "element of transposed matrix")
  expect(x:getitem({ 3, 1 }), x:transpose():getitem({ 1, 3 }), "element of transposed matrix")
end

test_matrix_transpose()

local function test_matrix_addition()
  local x = matrix.Matrix:new({ { 1, 2 } })
  local y = matrix.Matrix:new({ { 3, 4 } })
  local z = matrix.Matrix:new({ { 4, 6 } })

  expect(z, x + y, "matrix addition")

  local a = matrix.Matrix:new({ { autograd.Value:new(7), autograd.Value:new(8) } })
  local b = matrix.Matrix:new({ { autograd.Value:new(9), autograd.Value:new(10) } })

  -- c == d := (7+9, 8+10)
  local c = matrix.Matrix:new({ { autograd.Value:new(16), autograd.Value:new(18) } })
  local d = a + b

  expect(c, d, "matrix addition with autograd (7,9) + (8,10)")

  d:getitem({ 1, 1 }):backward()
  expect(1, a:getitem({ 1, 1 }).grad, "gradient of 9+x wrt x")
  expect(0, a:getitem({ 1, 2 }).grad, "gradient of 9+x wrt y")
  expect(1, b:getitem({ 1, 1 }).grad, "gradient of 7+x wrt x")
end

test_matrix_addition()

local function test_matrix_multiplication()
  local x = matrix.Matrix:new({ { 1, 2 } })
  local y = matrix.Matrix:new({ { 3, 4 }, { 5, 6 } })

  local a = matrix.Matrix:new({ { 13, 16 } })
  local b = matrix.Matrix:new({ { 11 }, { 17 } })

  expect(a, x * y, "matmul x@y")

  x = x:transpose()

  expect(b, y * x, "matmul y@x^T")

  local t = matrix.Matrix:new({ { autograd.Value:new(1), autograd.Value:new(2) } })
  local u = matrix.Matrix:new({ { autograd.Value:new(3), autograd.Value:new(4) } })
  u = u:transpose()

  -- v == w := 1*3 + 4*2
  local v = matrix.Matrix:new({ { autograd.Value:new(11) } })
  local w = t * u

  expect(v, w, "matmul with autograd (1,3) @ (3,4)^T")
  w:getitem({ 1, 1 }):backward()

  expect(3, t:getitem({ 1, 1 }).grad, "gradient of 3x + 4*2 wrt x")
  expect(2, u:getitem({ 2, 1 }).grad, "gradient of 3*1 + 2x wrt x")
end

test_matrix_multiplication()
