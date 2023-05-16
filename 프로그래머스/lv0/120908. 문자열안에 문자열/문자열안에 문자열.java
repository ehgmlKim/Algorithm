class Solution {
    public int solution(String str1, String str2) {
        int answer = 1;
        String[] arr = str1.split(str2);
        
        for(String a : arr){
            if(a.equals(str1))
                answer = 2;
        }
        return answer;
    }
}