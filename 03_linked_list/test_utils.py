from linked_list import list_node

def gen_list_of_len(n):
	result = list_node()
	curr = result
	i = -1
	for i in xrange(n - 1):
		curr.val = i
		curr.next_ = list_node()
		curr = curr.next_

	curr.val = i + 1

	return result
