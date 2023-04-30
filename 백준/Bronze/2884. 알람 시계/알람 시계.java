import java.util.Scanner;

class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
        int m = sc.nextInt();
        
		if(m>=45){
            m = m-45;
        }else{
            h = h-1;
            m = m+60-45;
        }
        if(h<0)
            h = h+24;
        System.out.println(h+" "+m);
    }
}