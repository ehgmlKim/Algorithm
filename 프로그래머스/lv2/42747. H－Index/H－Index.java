import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int len = citations.length;
        int max = 0;
        for(int i=len;i>0;i--){
            int cnt = 0;
            for(int c : citations){
                if(c>=i)
                    cnt++;
            }
            if(cnt>=i)
                max = (i>max) ? i : max;
        }
        return max;
    }
}