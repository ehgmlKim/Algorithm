class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        int i = 0;
        for(String s : strlist){
            int len = s.length();
            answer[i] = len;
            i++;
        }
        return answer;
    }
}