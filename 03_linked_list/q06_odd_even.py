# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# The program should run in O(1) space complexity and O(nodes) time complexity.

from linked_list import advance, len_list


def reorder_odd_even(head_):
	odd_head = None
	odd_last = None
	even_head = None
	even_last = None
	curr = head_
	count = 1

	while curr:
		if count % 2 == 0:
			if not even_head:
				even_head = curr
				even_last = even_head
			else:
				even_last.next_ =  curr
				even_last = even_last.next_
		else:
			if not odd_head:
				odd_head = curr
				odd_last = odd_head
			else:
				odd_last.next_ =  curr
				odd_last = odd_last.next_

		curr = curr.next_
		count += 1

	even_last.next_ = odd_head

	return even_head
