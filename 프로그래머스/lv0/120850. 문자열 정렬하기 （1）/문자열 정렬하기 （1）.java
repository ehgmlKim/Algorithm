import java.util.*;
class Solution {
    public int[] solution(String my_string) {
        int cnt = 0;
        for(int i=0;i<my_string.length(); i++){
            char c = my_string.charAt(i);
            if(Character.isDigit(c))
                cnt += 1;
        }
        int[] answer = new int[cnt];
        int i = 0;
        for(String s : my_string.split("")){
            try{
                int a = Integer.parseInt(s);
                answer[i] = a;
                i++;
            } catch(Exception e){ }
        }
        Arrays.sort(answer);
        return answer;
    }
}