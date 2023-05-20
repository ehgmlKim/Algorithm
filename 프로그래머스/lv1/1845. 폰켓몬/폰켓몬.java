import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Arrays.sort(nums);
        int max = nums[nums.length-1];
        int num = nums.length/2;
        int[] arr = new int[max+1];
        for(int i=0;i<nums.length;i++){
            arr[nums[i]] += 1;
        }
        int cnt = 0; //포켓몬 종류
        for(int i=1;i<max+1;i++){
            if(arr[i]>0)
                cnt++;
        }
        answer = (cnt>num) ? num : cnt;
        return answer;
    }
}