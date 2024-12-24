class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Fungsi untuk mencetak elemen dari linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Fungsi untuk membuat linked list dari list Python
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Fungsi untuk membalikkan linked list secara rekursif
def reverse_linked_list_recursive(current, prev=None):
    if current is None:  # Basis rekursi: sampai akhir list
        return prev
    next_node = current.next  # Simpan node berikutnya
    current.next = prev       # Balik arah pointer
    return reverse_linked_list_recursive(next_node, current)

# Main: Uji algoritma rekursif
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)

    print("Original Linked List:")
    print_linked_list(head)

    print("\nReversed Linked List (Recursive):")
    reversed_head = reverse_linked_list_recursive(head)
    print_linked_list(reversed_head)
