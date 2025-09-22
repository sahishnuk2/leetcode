import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> idx = new HashMap<>();

        int len = nums.length;
        for (int i = 0; i < len; i++) {
            int index = idx.getOrDefault(nums[i], -1);
            if (index != i && index != -1) {
                return new int[] {i, index};
            }
            int key = target - nums[i];
            idx.put(key, i);
        }
        return null;
    }
}
