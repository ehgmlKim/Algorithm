import java.util.*;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        my_string = my_string.toLowerCase();
        String[] arr = my_string.split("");
        Arrays.sort(arr);
        for(String a : arr)
            answer += a;
        return answer;
    }
}