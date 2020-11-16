def maxArea(self, height):
        largest = 0
        head = 0
        tail = len(height)-1
        for i in range(len(height)-1):
            width = abs(head-tail)
            if height[head] < height[tail]:
                response = width  * height[head]
                head += 1
            else:
                response = width * height[tail]
                tail -= 1
            if response > largest:
                largest = response
        return largest