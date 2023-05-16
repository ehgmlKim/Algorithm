class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = new int[2];
        int denom = denom1*denom2;
        int numer = numer1*denom2 + numer2*denom1;
        int min = (denom>numer) ? numer : denom;
        for(int i=min;i>0;i--){
            if(numer%i==0 && denom%i==0){
                denom /= i;
                numer /= i;
            }      
        }
        answer[0] = numer;
        answer[1] = denom;
        return answer;
    }
}