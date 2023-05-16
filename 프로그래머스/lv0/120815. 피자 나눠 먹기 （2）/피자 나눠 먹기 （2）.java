class Solution {
    public int solution(int n) {
        int answer = 0;
        int min = (n>6) ? 6 : n;
        for(int i=min; i<=6*n;i++){
            if(i%6==0 && i%n==0){
                answer = i;
                break;
            }
        }
        return answer/6;
    }
}