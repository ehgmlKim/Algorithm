import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] arr = new String[numbers.length];
        int i = 0;
        for(int n : numbers){
            String s = "";
            for(int j=0;j<3;j++)
                s+=String.valueOf(n);
            arr[i++] = s;
        }
        Arrays.sort(arr);
        
        for(String s : arr){
            int len = s.length();
            answer = s.substring(0, len/3) + answer;
        }
        if(answer.startsWith("0"))
            answer = "0";
        return answer;
    }
}