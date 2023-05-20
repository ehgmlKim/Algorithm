import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int w = 0;
        int h = 0;
        for(int[] a : sizes){
            Arrays.sort(a);
            w = (w<a[0]) ? a[0] : w;
            h = (h<a[1]) ? a[1] : h;
        }
        return w*h;
    }
}