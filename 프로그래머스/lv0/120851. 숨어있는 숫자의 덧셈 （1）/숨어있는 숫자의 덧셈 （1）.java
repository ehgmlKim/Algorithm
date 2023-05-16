class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(String s : my_string.split("")){
            try{
                int i = Integer.parseInt(s);
                answer += i;
            }catch(Exception e ){
                
            }
        }
        return answer;
    }
}