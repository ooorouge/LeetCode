* 快慢两个标记点，一个```count```统计正确的个数，一个```i```遍历数组，只开了一个count
* 如果找到一个比```nums[count]```大的```nums[i]```，那么```nums[++count] = nums[i]```，然后循环结束，```++i```，如果相等，那么只有循环结束```++i```
其余不变化

```c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int counter = 0;
        if(nums.size() < 2){
            return nums.size();
        }
        for(int i = 1; i < nums.size(); ++i){
            if(nums[i] > nums[counter]){
                nums[++counter] = nums[i];
            }
        }
        return counter+1;
    }
};
```

* 边界边界，空和只有一个的array直接返回size就行了
* vector<int>& nums
