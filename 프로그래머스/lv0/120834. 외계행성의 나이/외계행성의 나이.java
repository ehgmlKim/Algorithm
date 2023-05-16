class Solution {
    public String solution(int age) {
        String answer = "";
        String alpa ="abcdefghijklmnopqrstuvwxyz";
        String[] arr = alpa.split("");
        while(age>0){
            int i = age%10;
            age /= 10;
            answer += arr[i];
        }
        StringBuffer sb = new StringBuffer(answer);
        answer = sb.reverse().toString();
        return answer;
    }
}