# coding=utf-8
# Given a singly linked list L: L0→L1→ ... →Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→...

# For example, given {1,2,3,4}, reorder it to {1,4,2,3}. You must do this in-place without altering the nodes' values.
# For example, given {1,2,3,4,5,6}, reorder it to {1,6,2,5,3,4}. You must do this in-place without altering the nodes' values.

from linked_list import advance, len_list, print_list


def reorder_list(head_):
	len_ = len_list(head_)
	to_move = (len_ + 1) / 2 - 1
	moved = 0
	curr = head_
	
	print_list(head_)
	while moved < to_move:
		before_to_insert = advance(head_, len_ - 2)
		before_to_insert.next_.next_ = curr.next_
		curr.next_ = before_to_insert.next_
		before_to_insert.next_ = None
		curr = curr.next_.next_
		moved += 1

		print_list(head_)


	return head_
