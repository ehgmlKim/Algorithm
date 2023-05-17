import java.util.*;
class Solution {
    public int solution(int[] array, int n) {
        int[] dis = new int[array.length];
        for(int i=0;i<array.length;i++){
            dis[i] = Math.abs(array[i]-n);
        }
        int min = dis[0];
        for(int i=0;i<array.length;i++){
            if(min>dis[i]){
                min = dis[i];
            }
        }
        ArrayList<Integer> list = new ArrayList();
        for(int i=0;i<array.length;i++){
            if(dis[i] == min){
                list.add(array[i]);
            }
        }
        Collections.sort(list);
        return list.get(0);
    }
}