class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int len = numbers.length;
        for(int n : numbers){
            answer += n;
        }
        return answer/len;
    }
}