def level_order_traversal(root):
    if root == None:
        return

    result =""
    queues = [deque(),deque()]
    current_queue = queues[0]

    next_queue = queues[1]

    current_queue.append(root)

    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        print(str(temp.data), end =" ")
        result += str(temp.data)+ " "

        if temp.left !=None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.right)


        if not current_queue:
            print()
            level_number+=1
            current_queue = queues[level_number%2]
            next_queue = queues[(level_number+1) % 2]
    print()
    return result


#Solution 2
#O(n)|O(n)
# Using one queue
def level_order_traversal(root):
  if root == None:
    return

  result = ""

  current_queue = deque()
  current_queue.append(root)
  current_queue.append(None)

  while len(current_queue) != 0:
    temp = current_queue.popleft()
    print(str(temp.data), end = " ")
    result += str(temp.data) + " "

    if temp.left != None:
      current_queue.append(temp.left)

    if temp.right != None:
      current_queue.append(temp.right)

    if current_queue[0] == None:
      print()
      current_queue.popleft()

      if len(current_queue) != 0:
        current_queue.append(None)

  print()
  return result





#Solution 3
#O(n^2)|O(n)
# Compute the maximum height of a tree
def get_max_height(node):
  if node is None:
    return 0
  else :
    left_height = get_max_height(node.left)
    right_height = get_max_height(node.right)

    # Return the larger value
    return left_height+1 if left_height > right_height else right_height+1

# get nodes at a specific level
def get_h_level_order(root , level, output):
  if root is None:
    return
  if level == 1:
    print(root.data, end=" ")
    output.append(str(root.data))
  elif level > 1 :
    get_h_level_order(root.left , level-1, output)
    get_h_level_order(root.right , level-1, output)

def level_order_traversal(root):
  h = get_max_height(root)
  output = []
  for i in range(1, h+1):
    get_h_level_order(root, i, output)
    print()
  return ' '.join(output)

arr = [100,50,200,25,75,350,400]
root = create_BST(arr)

print("\nLevel Order Traversal:\n", end = "")
level_order_traversal(root)