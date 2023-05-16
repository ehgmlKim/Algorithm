class Solution {
    public int solution(int n, int k) {
        int answer = n*12000+k*2000; //원래 내야하는 값
        int cut = n/10*2000; //할인 받은 가격
        return answer-cut;
    }
}