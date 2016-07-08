import linked_list as ll
import test_utils as tu
from q05_merge_sorted import merge_sorted

for len_1, len_2 in [(6, 6), (1, 1), (3, 3), (6, 9), (1, 3), (0, 5)]:
	l1 = tu.gen_list_of_len(len_1)
	ll.print_list(l1)
	
	l2 = tu.gen_list_of_len(len_2)
	ll.print_list(l2)

	ll.print_list(merge_sorted(l1, l2))
