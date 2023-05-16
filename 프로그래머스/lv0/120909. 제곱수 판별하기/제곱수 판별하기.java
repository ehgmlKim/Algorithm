class Solution {
    public int solution(int n) {
        int answer = 2;
        double m = Math.sqrt(n);
        if (m == (int)m) answer =  1;
        return answer;
    }
}