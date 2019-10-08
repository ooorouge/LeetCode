### K Closest类型题目，Amazon OA
* 思路就是创建一个最大堆，当堆的size大于k之后，删除堆顶（最大值）剩下的就会一直是最小个K，然后就是重载比较符号的办法
```java
PriorityQueue<int[]> pq = new PriorityQueue<int[]> (K, new Comparator<int[]> () {
            @Override
            public int compare(int[] a, int[] b) {
                return (int) (b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]);
            }
        });
        // a理解为当前堆顶，b是正在加入堆的值，如果b比a大，那么b距离-a距离大于0，return大于0，b放在堆顶
```
```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        
        PriorityQueue<int[]> pq = new PriorityQueue<int[]> (K, new Comparator<int[]> () {
            @Override
            public int compare(int[] a, int[] b) {
                return (int) (b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]);
            }
        });
        
        for (int i = 0; i < points.length; ++i) {
            pq.offer(points[i]);
            if (pq.size() > K ) {
                pq.poll();
            }
        }
        int[][] ans = new int[K][2];
        for (int i = 0; i < K; ++i) {
            ans[i] = pq.poll();
        }
        return ans;
    } 
}
```
