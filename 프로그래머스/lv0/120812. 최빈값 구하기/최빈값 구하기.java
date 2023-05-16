import java.util.*;
class Solution {
    public int solution(int[] array) {
        Arrays.sort(array);
        int len = array[array.length-1];
        int[] arr = new int[len+1];
        for(int a : array){
            arr[a]++;
        }
        int max = -1;
        int idx = -1;
        for(int i=0;i<len+1;i++){
            if(arr[i]>max){
                max = arr[i];
                idx = i;
            }
        }
        //최빈값의 개수
        int cnt = 0;
        for(int a : arr){
            if(a==max)
                cnt++;
        }
        return (cnt>1) ? -1 : idx;
    }
}