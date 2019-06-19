* No 21 Merge Two Sorted Lists
* 就是一个基础的链表练习
* 注意点
  * 用一个```dummy``` 加 一个```*cur``` 保证 ```cur = cur->next```后链表第一个位置不会掉
  * 一个链表用完了不要忘了把剩下一个的剩余部分贴上去
  ```c++
 //Definition for singly-linked list.
 // struct ListNode {
 //     int val;
 //     ListNode *next;
 //     ListNode(int x) : val(x), next(NULL) {}
 // };
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy = ListNode(INT_MIN);
        ListNode *cur = &dummy;        
        while(l1 && l2) {
            if(l1->val < l2->val) {
                cur->next = l1;
                l1 = l1->next;
            }
            else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 ? l1 : l2;
        return dummy.next;
    }
};
```
