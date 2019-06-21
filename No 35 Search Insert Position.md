* 二分查找问题
* 注意很多边界点：
  * t在r右，t在l左，t==r, t==l;从第一步就要考虑这四个情况
  * 取了middle之后要算一下nextmiddle的大小来确定下一个边界点是哪两组
  * 最好r - l > 1,== 1意味着找不到t
```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int dur = right - left;
        if(nums[left] >= target){return 0;}
        if(nums[right] < target){return right+1;}
        if(nums[right] == target){return right;}
        while(dur > 1){
            if(nums[left] == target){return left;}
            if(nums[right] == target){return right;}
            int middle = int((right+left) / 2);
            if(nums[middle] == target){return middle;}
            
            if(nums[middle] > target){
                int nextmiddle = int((left+middle) / 2);
                if(nums[nextmiddle] == target){return nextmiddle;}
                if(nums[nextmiddle] > target){
                    right = nextmiddle;
                }
                if(nums[nextmiddle] < target){
                    left = nextmiddle;
                    right = middle;
                }
            }
            
            if(nums[middle] < target){
                int nextmiddle = int((right+middle) / 2);
                if(nums[nextmiddle] == target){return nextmiddle;}
                if(nums[nextmiddle] > target){
                    left = middle;
                    right = nextmiddle;
                }
                if(nums[nextmiddle] < target){
                    left = nextmiddle;
                }
            }
            dur = right - left;
        }
        return right;
    }
};
```
