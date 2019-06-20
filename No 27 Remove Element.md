* 和26很像，都是in-place O(1)
* 唯一一点不同是vector只有val,所以输出应该是0，并且vector应该```.clear()```,将遇到的第一个非val放到```nums[0]```，所以遍历完之后如果
```nums[0] != val```就行了，反之清空整个vector
```c++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        if(nums.size() == 0){
            return 0;
        }
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] != val){
                nums[count++] = nums[i];
            }
        }
        if(nums[0] == val){
            nums.clear();
            return 0;
        }
        return count;
    }
};
```
