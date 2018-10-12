class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = []
    # x = self.value
    # if x:
    #   if self.left:
    #     self.depth_first_for_each(self.left)
    #   if self.right:
    #     self.depth_first_for_each(self.right)
    # return lambda x: stack.append(x)   
    if self.value is not None:
      stack.append(self.value)
      # return cb = lambda x: stack.append(x)
      if self.left:
        # stack.append(self.left.value)
        # return lambda: self.left.depth_first_for_each(self.left)
        return self.left.depth_first_for_each(lambda x: stack.append(x))
      if self.right:
        # stack.append(self.right.value)
        # return lambda: self.right.depth_first_for_each(self.right)
        return self.right.depth_first_for_each(lambda x: stack.append(x))


  def breadth_first_for_each(self, cb):
    return lambda x: x + n

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
