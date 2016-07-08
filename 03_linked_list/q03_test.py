import linked_list as ll
import test_utils as tu
from q03_has_cycle import has_cycle

print(has_cycle(tu.gen_list_of_len(10)))
print(has_cycle(tu.gen_list_with_loop(10, 20)))
print(has_cycle(tu.gen_list_with_loop(1, 0)))
