import java.util.LinkedHashMap;
import java.util.Map;

public class LRU {
    public static void main(String[] args) {

        LRUCache obj = new LRUCache(2);
//        obj.put(1, 1);
//        obj.put(2, 2);
//        System.out.println(obj.get(1));
//        obj.put(3, 3);
//        System.out.println(obj.get(2));
//        obj.put(4, 4);
//        System.out.println(obj.get(1));
//        System.out.println(obj.get(3));
//        System.out.println(obj.get(4));
        // ["LRUCache","get","put","get","put","put","get","get"]
        //[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
//        System.out.println(obj.get(2));
//        obj.put(2, 6);
//        System.out.println(obj.get(1));
//        obj.put(1, 5);
//        obj.put(1, 2);
//        System.out.println(obj.get(1));
//        System.out.println(obj.get(2));
        //["LRUCache","put","put","put","put","get","get"]
        //[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
        obj.put(2, 1);
        obj.put(1, 1);
        obj.put(2, 3);
        obj.put(4, 1);
        System.out.println(obj.get(1));
        System.out.println(obj.get(2));
    }
}

class LRUCache {
    private final int CAPACITY;
    private LinkedHashMap<Integer, Integer> cache;

    public LRUCache(int capacity) {
        CAPACITY = capacity;
        cache = new LinkedHashMap<>(CAPACITY, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > CAPACITY;
            }
        };
    }

    public int get(int key) {
        return cache.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        cache.put(key, value);
    }
}
