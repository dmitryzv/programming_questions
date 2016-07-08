# coding=utf-8
# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Assumptions:
# No loops
# Returns new list

from linked_list import list_node, copy_list


def add_nodewise(head_1, head_2):
	if not head_1 and not head_2:
		return None

	result_head = None
	result_curr = None
	
	curr_1 = head_1
	curr_2 = head_2

	carry = 0
	while curr_1 and curr_2:
		sum_ = curr_1.val + curr_2.val + carry
		
		if not result_head:
			result_curr = list_node()
			result_head = result_curr
		else:
			result_curr.next_ = list_node()
			result_curr = result_curr.next_

		result_curr.val = sum_ % 10
		carry = 1 if sum_ >= 10 else 0

		curr_1 = curr_1.next_
		curr_2 = curr_2.next_

	# copy the remainder of longer list
	last_node_before_copy = None

	if carry > 0:
		last_node_before_copy = result_curr

	to_copy = curr_1 if not curr_2 else curr_2
	if not result_curr:
		result_curr = copy_list(to_copy)
		result_head = result_curr
	else:		
		result_curr.next_ = copy_list(to_copy)

	if last_node_before_copy:
		if not last_node_before_copy.next_:
			last_node_before_copy.next_ = list_node()
			last_node_before_copy.next_.val = 0

		last_node_before_copy.next_.val += 1

	return result_head
