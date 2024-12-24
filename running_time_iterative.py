import time

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Fungsi untuk mencetak elemen dari linked list (opsional untuk debug)
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

# Fungsi untuk membalikkan linked list secara iteratif
def reverse_linked_list_iterative(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Simpan pointer ke node berikutnya
        current.next = prev       # Balik arah pointer
        prev = current            # Pindahkan prev ke current
        current = next_node       # Lanjutkan ke node berikutnya
    return prev

# Fungsi untuk mengukur waktu eksekusi
def measure_execution_time():
    input_sizes = [10, 100, 1000, 10000, 50000, 100000]  # Berbagai ukuran input
    execution_times = []

    for size in input_sizes:
        # Buat linked list dengan ukuran tertentu
        values = list(range(size))
        head = create_linked_list(values)

        # Catat waktu mulai
        start_time = time.time()

        # Jalankan algoritma
        reverse_linked_list_iterative(head)

        # Catat waktu selesai
        end_time = time.time()

        # Hitung waktu eksekusi
        execution_time = end_time - start_time
        execution_times.append((size, execution_time))

    # Cetak hasil
    print("Input Size\tExecution Time (s)")
    for size, exec_time in execution_times:
        print(f"{size}\t\t{exec_time:.6f}")

if __name__ == "__main__":
    measure_execution_time()
