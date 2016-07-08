# Given a linked list, determine if it has a cycle in it.

from linked_list import *

def has_cycle(head_):
	runner_1 = head_
	runner_2 = head_.next_

	while runner_2 and runner_1:

		if runner_1 == runner_2:
			return True

		runner_1 = runner_1.next_
		runner_2 = runner_2.next_.next_ if runner_2.next_ else None

	return False
