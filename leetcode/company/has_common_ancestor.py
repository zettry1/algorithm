
# https://leetcode.com/discuss/interview-question/786821/Indeed-or-OA-2020-or-Parents-and-Children-(Graph)
def has_common_ancestor(parent_child_pairs, node1, node2):

  dic = {}
  for pair in parent_child_pairs:
    if pair[1] not in dic:
        dic[pair[1]] = [pair[0]]
    else:
        dic.get(pair[1]).append(pair[0])

    # if child not in dic:
    #     dic[child] = [parent]
    # else:
    #     dic.get(child).append(parent)


  def helper(dic, parents, node):
      if not node or node not in dic:
          return

      for x in dic.get(node):
          parents.append(x)
          helper(dic, parents, x)

  p1, p2 = [], []

  helper(dic,p1,node1)
  helper(dic,p2,node2)

  return len(p2) + len(p1) != len(set((p2 + p1)))
