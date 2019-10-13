### 做深拷贝，deep copy，核心思想就是不允许引用拷贝，那就重新创建一次
* 其实，第一个办法基本不会出错，用就完事
```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {
            return null;
        }
        
        HashMap<Node, Node> hm = new HashMap<>();
        
        Node cur = head;
        while (cur != null) {
            hm.put(cur, new Node(cur.val));
            cur = cur.next;
        }
        
        cur = head;
        while (cur != null) {
            if (cur.next != null) {
                hm.get(cur).next = hm.get(cur.next);
            }
            if (cur.random != null) {
                hm.get(cur).random = hm.get(cur.random);
            }
            cur = cur.next;
        }
        return hm.get(head);
    }
}
```
```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) {return null;}
        
        Node start = head;
        while (start != null) {
            Node next = start.next;
            start.next = new Node(start.val);
            start.next.next = next;
            start = next;
        }
        
        start = head;
        while (start != null) {
            if (start.random != null) {
                //random.next 是指向random后面那个副本，所以必须.next
                start.next.random = start.random.next;
            }
            // 跳两格
            start = start.next.next;
        }
        
        start = head;
        Node copyhead = head.next;
        Node copystart = copyhead;
        while (copystart.next != null) {
            start.next = start.next.next;
            start = start.next;
            
            copystart.next = copystart.next.next;
            copystart = copystart.next;
        }
        start.next = start.next.next;
        return copyhead;
}
}
```
