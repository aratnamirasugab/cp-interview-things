package IntersectionofTwoArrays;

import java.util.*;

public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        if (nums1 == null || nums2 == null) {
            return new int[0];
        }
        
        List<Integer> result = new ArrayList<>();
        Set <Integer> set = new HashSet<>();
        for (int item : nums1) {
            set.add(item);
        }
        
        for (int item : nums2) {
            if (set.contains(item)) {
                result.add(item);
                set.remove(item);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();

    }    
}
