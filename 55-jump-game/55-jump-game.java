class Solution {
    public boolean canJump(int[] nums) 
    {

        for(int i = 0; i<nums.length-1; i++)
        {
            if (nums[i] ==0){
                return false;
            }
            nums[i+1] = Math.max(nums[i]-1, nums[i+1]);
                
        }
        return true;
    }
}
