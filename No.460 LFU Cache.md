### No.460 LFU Cache
* 比较复杂的情况下先写好注释再慢慢填充
* 用了hashmap和table，时间和空间都比较优秀的用doublelinkedlist写的
```class LFUCache {
    private HashMap<Integer, Integer> map;
    private HashMap<Integer, Integer> count;
    private HashMap<Integer, LinkedHashSet<Integer>> lists;
    private int min;
    private int cap;
    
    public LFUCache(int capacity) {
        cap = capacity;
        min = -1;
        map = new HashMap<Integer, Integer>();
        count = new HashMap<Integer, Integer>();
        lists = new HashMap<Integer, LinkedHashSet<Integer>>();
        lists.put(1, new LinkedHashSet<Integer>());
    }
    
    public int get(int key) {
        //get之后会影响count和lists和可能影响全局min
        //对于count的影响很简单，更新value
        //对于lists的影响，第一，从原来在的LinkedHashSet删除，换到count+1 key对应的LinkedHashSet
        //                          ^没有边界情况可以直接写
        //                                                    ^count+1 对应的会不会不存在？
        //对于全局min
        //如果`count==min`，不能直接更新，需要检查全局min对应的LinkedHashSet
        //tiaozheng freq
        if (!map.containsKey(key)) {return -1;}
        int ct = count.get(key);
        //tiaozheng count tiaozheng lists
        count.put(key, ct+1);
        lists.get(ct).remove(key);
        //min de list
        if (ct == min && lists.get(ct).size() == 0) {
            min += 1;
        }
        //不存在
        if (!lists.containsKey(ct+1)) {
            lists.put(ct+1, new LinkedHashSet<Integer>());
        }
        lists.get(ct+1).add(key);
        return map.get(key);
    }
    
    public void put(int key, int value) {
        //put一个值出现的几种情况
        //首先，cap=0的边界情况，这个时候put不会引起任何变化
        //其一，key值已经存在过了，那么直接替换，并且put一个已经存在的key也相当于get了这个key一次，不要漏写，做完return
        //其二，map满了，删除min对应的linkedlist的第一个，因为第一个是leastrecent
        //新的，且没有满
        //gaidong min = 1
        if (cap <= 0) {
            return ;
        }
        //1.yijing cunzai
        if (map.containsKey(key)) {
            map.put(key, value);
            get(key);
            return ; //!!!!
        }
        //2.manle
        if (map.size() == this.cap) {
            //shan yige zuibuyongde
            int del = lists.get(min).iterator().next();
            lists.get(min).remove(del);
            count.remove(del);
            map.remove(del);
        }
        //3.zhengchangqingkuang
        map.put(key, value);
        count.put(key, 1);
        lists.get(1).add(key);
        min = 1;
    }
}
```
