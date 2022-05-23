
class Solution {
    public int longestConsecutive(int[] nums) {
        int result = 0;
        Set<Integer> integers = new HashSet<>();
        // This is to remove any duplicate value that the array may contain
        for (int n : nums){
            integers.add(n);
        }
        
        for(int i=0;i<nums.length;i++){
            int currentValue = nums[i];
            if(!integers.contains(currentValue-1)){
                /* This is the first value
                we increment this value looking if there is an value present if not we continue the loop
                */
                while(integers.contains(currentValue)){
                    currentValue++;
                }
               //check if incremental value is larger that the value incrementend if so re asign the result
            if(currentValue-nums[i]>result){
                result = currentValue - nums[i];
            }
            }
        }
        return result;
    }
}