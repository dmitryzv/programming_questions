# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

from linked_list import *


def merge_sorted(head_1, head_2):
	if not head_1 and not head_2:
			return None

	result_head = None
	result_curr = None
	
	curr_1 = head_1
	curr_2 = head_2

	while curr_1 and curr_2:
		if not result_head:
			result_curr = list_node()
			result_head = result_curr
		else:
			result_curr.next_ = list_node()
			result_curr = result_curr.next_

		if curr_1.val <= curr_2.val:
			result_curr.val = curr_1.val
			curr_1 = curr_1.next_
		else:
			result_curr.val = curr_2.val
			curr_2 = curr_2.next_

	to_copy = curr_1 if not curr_2 else curr_2

	if not result_curr:
		result_curr = copy_list(to_copy)
		result_head = result_curr
	else:		
		result_curr.next_ = copy_list(to_copy)

	return result_head
