import java.util.*;

class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
        
		int max = 0;
        int x = 0;
        int y = 0;
		for(int i=0;i<9;i++){
		    for(int j=0;j<9;j++){
			    int a = sc.nextInt();
                if(a>max){
                    max = a;
                    x = i;
                    y = j;
                }
		    }
		}

		System.out.println(max);
        System.out.println((x+1)+" "+(y+1));
        
	}
}