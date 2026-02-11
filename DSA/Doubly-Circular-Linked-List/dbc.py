# ------------------- নোড ক্লাস -------------------
class Node:
    def __init__(self, data):
        self.data = data        # নোডের মান
        self.prev = None        # আগের নোড
        self.next = None        # পরের নোড


# -------- ডাবলি সার্কুলার লিঙ্কড লিস্ট ক্লাস --------
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None        # লিস্টের শুরু

    # ১. শুরুতে নতুন মান যোগ করা
    def insert_beginning(self, value):
        new_node = Node(value)

        if self.head is None:
            # লিস্ট খালি → নোড নিজেই নিজের সাথে যুক্ত
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(f"{value} → প্রথম নোড হিসেবে যুক্ত হয়েছে")
            return

        last = self.head.prev           # শেষ নোড
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        self.head = new_node
        print(f"{value} → শুরুতে যুক্ত হয়েছে")

    # ২. শেষে নতুন মান যোগ করা
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            print(f"{value} → প্রথম নোড হিসেবে যুক্ত হয়েছে")
            return

        last = self.head.prev
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node
        print(f"{value} → শেষে যুক্ত হয়েছে")

    # ৩. কোনো মানের পরে যোগ করা
    def insert_after(self, prev_value, value):
        if not self.head:
            print("লিস্ট খালি আছে")
            return

        temp = self.head
        while True:
            if temp.data == prev_value:
                new_node = Node(value)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                print(f"{value} → {prev_value} এর পরে যুক্ত হয়েছে")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{prev_value} পাওয়া যায়নি")

    # ৪. সামনে থেকে দেখানো (Forward)
    def show_forward(self):
        if not self.head:
            print("লিস্ট খালি")
            return

        print("লিস্ট (সামনে থেকে): ", end="")
        temp = self.head
        while True:
            print(temp.data, end=" → ")
            temp = temp.next
            if temp == self.head:
                break
        print("(শুরুতে ফিরে এসেছে)")

    # ৫. পিছন থেকে দেখানো (Backward)
    def show_backward(self):
        if not self.head:
            print("লিস্ট খালি")
            return

        print("লিস্ট (পিছন থেকে): ", end="")
        temp = self.head.prev           # শেষ নোড
        start = temp
        while True:
            print(temp.data, end=" → ")
            temp = temp.prev
            if temp == start:
                break
        print("(শেষে ফিরে এসেছে)")

    # ৬. কোনো মান খোঁজা
    def search(self, key):
        if not self.head:
            print("লিস্ট খালি")
            return

        temp = self.head
        pos = 1
        while True:
            if temp.data == key:
                print(f"{key} পাওয়া গেছে → অবস্থান {pos}")
                return
            temp = temp.next
            pos += 1
            if temp == self.head:
                break
        print(f"{key} পাওয়া যায়নি")

    # ৭. কয়টা নোড আছে গণনা করা
    def count(self):
        if not self.head:
            print("মোট নোড: 0")
            return 0

        cnt = 0
        temp = self.head
        while True:
            cnt += 1
            temp = temp.next
            if temp == self.head:
                break
        print(f"মোট নোড: {cnt}")
        return cnt

    # ৮. শুরু থেকে মুছে ফেলা
    def delete_beginning(self):
        if not self.head:
            print("লিস্ট খালি")
            return

        if self.head.next == self.head:
            print(f"{self.head.data} মুছে ফেলা হয়েছে (শুধু একটা নোড)")
            self.head = None
            return

        last = self.head.prev
        deleted = self.head.data
        self.head = self.head.next
        self.head.prev = last
        last.next = self.head
        print(f"{deleted} শুরু থেকে মুছে ফেলা হয়েছে")

    # ৯. শেষ থেকে মুছে ফেলা
    def delete_end(self):
        if not self.head:
            print("লিস্ট খালি")
            return

        if self.head.next == self.head:
            print(f"{self.head.data} মুছে ফেলা হয়েছে (শুধু একটা নোড)")
            self.head = None
            return

        last = self.head.prev
        deleted = last.data
        new_last = last.prev
        new_last.next = self.head
        self.head.prev = new_last
        print(f"{deleted} শেষ থেকে মুছে ফেলা হয়েছে")

    # ১০. নির্দিষ্ট মান মুছে ফেলা
    def delete(self, key):
        if not self.head:
            print("লিস্ট খালি")
            return

        temp = self.head
        while True:
            if temp.data == key:
                if temp.next == temp:                   # একটা নোড
                    print(f"{key} মুছে ফেলা হয়েছে (শুধু একটা নোড)")
                    self.head = None
                    return
                if temp == self.head:                   # হেড মুছছি
                    self.delete_beginning()
                    return
                # সাধারণ কেস
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                print(f"{key} মুছে ফেলা হয়েছে")
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{key} পাওয়া যায়নি")


# ----------------- টেস্ট করা -----------------
if __name__ == "__main__":
    dcll = DoublyCircularLinkedList()

    print("\n===== ডাবলি সার্কুলার লিঙ্কড লিস্ট =====")

    print("\n→ যোগ করা হচ্ছে:")
    dcll.insert_beginning(10)
    dcll.insert_beginning(5)
    dcll.insert_end(20)
    dcll.insert_end(30)
    dcll.insert_after(20, 25)

    print("\n→ দেখানো হচ্ছে:")
    dcll.show_forward()
    dcll.show_backward()

    print("\n→ খোঁজা হচ্ছে:")
    dcll.search(25)
    dcll.search(99)

    print("\n→ নোড গণনা:")
    dcll.count()

    print("\n→ মুছে ফেলা হচ্ছে:")
    dcll.delete_beginning()
    dcll.show_forward()

    dcll.delete_end()
    dcll.show_forward()

    dcll.delete(20)
    dcll.show_forward()

    dcll.count()

    print("\n===== শেষ =====")