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

def gen_list_with_loop(before_loop, in_loop):
	result = list_node()
	curr = result
	i = -1
	to_link = result
	for i in xrange(before_loop + in_loop - 1):
		curr.val = i
		curr.next_ = list_node()
		if i == before_loop:
			to_link = curr
		curr = curr.next_

	curr.val = i + 1
	curr.next_ = to_link

	return result
