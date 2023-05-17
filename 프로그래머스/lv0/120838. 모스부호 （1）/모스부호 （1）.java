class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] morse = {".-","-...","-.-.","-..",".","..-.",
                "--.","....","..",".---","-.-",".-..","--","-.",
                "---",".--.","--.-",".-.","...","-","..-","...-",
                ".--","-..-","-.--","--.."};
        for(String l : letter.split(" ")){
            for(int i=0;i<26;i++){
                if(l.equals(morse[i]))
                    answer += Character.toString(i + 'a');
            }
        }
        return answer;
    }
}