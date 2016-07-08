class list_node(object):
	next_ = None
	val = 0

def copy_list(head_):
	if not head_:
		return None

	result_head = None

	result_curr = result_head
	curr = head_

	visited_nodes = {}

	while curr and not curr in visited_nodes:
		if not result_curr:
			result_curr = list_node()
			result_head = result_curr
		else:
			result_curr.next_ = list_node()
			result_curr = result_curr.next_

		result_curr.val = curr.val
		
		visited_nodes[curr] = True

		curr = curr.next_

	return result_head

def len_list(head_):
	result = 0

	curr = head_
	while curr:
		result += 1
		curr = curr.next_

	return result

def advance(head_, n):
	result = head_
	count = 0
	while result and count < n:
		result = result.next_
		count += 1

	return result

def print_list(head_):
	curr = head_
	to_print = []
	visited_nodes = {}
	while curr and curr not in visited_nodes:
		to_print.append(str(curr.val))
		visited_nodes[curr] = True
		curr = curr.next_

	print('->'.join(to_print))
