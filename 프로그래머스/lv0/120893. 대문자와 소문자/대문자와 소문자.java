class Solution {
    public String solution(String my_string) {
        String answer = "";
        String up = my_string.toUpperCase();
        String down = my_string.toLowerCase();
        
        for(int i=0; i<my_string.length(); i++){
            char a = my_string.charAt(i);
            char u = up.charAt(i);
            char d = down.charAt(i);
            if(a == u)
                answer += d;
            else
                answer += u;
        }
        return answer;
    }
}