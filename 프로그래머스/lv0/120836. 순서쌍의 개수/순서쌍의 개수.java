class Solution {
    public int solution(int n) {
        int answer = 0;
        double m = Math.sqrt(n);
        if (n==1) return 1;
        for(int i=1;i<m;i++){
            if(n%i==0)
                answer += 2;
        }
        if (m == (int)m) answer += 1;
        return answer;
    }
}