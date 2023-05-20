import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int len = commands.length;
        int[] answer = new int[len];
        for(int idx=0;idx<commands.length;idx++){
            int i = commands[idx][0];
            int j = commands[idx][1];
            int k = commands[idx][2];
            int[] temp = new int[j-i+1];
            int l = 0;
            for(int d = i-1; d<j; d++){
                temp[l++] = array[d];
            }
            Arrays.sort(temp);
            answer[idx] = temp[k-1];
        }
        return answer;
    }
}