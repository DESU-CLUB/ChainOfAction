```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l, r, pivot_index):
            pivot = nums[pivot_index]
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            store_index = l
            for i in range(l, r):
                if nums[i] > pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[store_index], nums[r] = nums[r], nums[store_index]
            return store_index
        
        def quick_select(l, r, kth_largest):
            if l == r:
                return nums[l]
            pivot_index = partition(l, r, r)
            if kth_largest == pivot_index:
                return nums[kth_largest]
            elif kth_largest < pivot_index:
                return quick_select(l, pivot_index - 1, kth_largest)
            else:
                return quick_select(pivot_index + 1, r, kth_largest)
        
        return quick_select(0, len(nums) - 1, k - 1)
```