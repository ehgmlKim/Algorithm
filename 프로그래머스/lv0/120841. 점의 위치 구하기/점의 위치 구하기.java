class Solution {
    public int solution(int[] dot) {
        int answer = 0;
        int x = dot[0];
        int y = dot[1];
        if (x*y>0){
            if(x>0)
                answer = 1;
            else
                answer = 3;
        } else{
            if(x>0)
                answer = 4;
            else
                answer = 2;
        }
        return answer;
    }
}