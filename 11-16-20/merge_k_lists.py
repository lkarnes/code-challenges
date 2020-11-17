def merge_k_list(self, lists):
        head = ListNode()
        current = head
        while len(lists) > 0 and lists != [None]:
            lowest = None
            low_list = None
            empty = None
            for index, i in enumerate(lists):
                if i != None:
                    if i.val < lowest or lowest == None:
                        lowest = i.val
                        low_list = index
                else: empty = index
            if lowest != None:
                current.next = ListNode(lowest)
                current = current.next
            if low_list != None:
                lists[low_list] = lists[low_list].next
            if empty != None:
                lists.pop(empty)
        return head.next