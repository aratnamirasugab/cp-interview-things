package IntersectionofTwoArraysII;

import java.util.*;

public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> hs_first = new HashMap<Integer, Integer>();
        Map<Integer, Integer> hs_two = new HashMap<Integer, Integer>();

        Arrays.sort(nums1);
        Arrays.sort(nums2);
        
        for (int item : nums1) {
            if (hs_first.containsKey(item)) {
                hs_first.put(item, hs_first.get(item) + 1);
            } else {
                hs_first.put(item, 1);
            }
        }

        for (int item : nums2) {
            if (hs_two.containsKey(item)) {
                hs_two.put(item, hs_two.get(item) + 1);
            } else {
                hs_two.put(item, 1);
            }
        }

        List <Integer> result = new ArrayList<>();
        Iterator entries = hs_first.entrySet().iterator();
        while (entries.hasNext()) {
            Map.Entry entry = (Map.Entry) entries.next();
            Integer key = (Integer)entry.getKey();
            Integer value = (Integer)entry.getValue();
            if (hs_two.containsKey(key)) {
                int valueLesser = value < hs_two.get(key) ? value : hs_two.get(key);
                
                int i = 0;
                while (i < valueLesser) {
                    result.add(key);
                    i++;
                }
                entries.remove();
            }
        }

        System.out.println(result);

        return result.stream().mapToInt(item -> item).toArray();
    }
}
