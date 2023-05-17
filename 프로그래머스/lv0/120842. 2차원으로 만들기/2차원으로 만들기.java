class Solution {
    public int[][] solution(int[] num_list, int n) {
        int len = num_list.length;
        int[][] answer = new int[len/n][n];
        for(int i=0;i<len/n;i++){
            int idx = 0;
            for(int j=n*i;j<n*i+n;j++){
                answer[i][idx++] = num_list[j];
            }
        }
        return answer;
    }
}