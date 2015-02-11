
public class solution2 {
	//public int d = 0;
	
	public int g(int n, int d){
		d = d+1;
		if (n == 0){
			System.out.format("current depth: %d \n",d);
			return 0;
		}
		else if (n == 1){
			System.out.format("current depth: %d \n",d);
			return 1;
		}
		else{
			return (int)Math.ceil(Math.sqrt(n))+5*g((int)Math.floor(4.0/7*n),d)
					+10*g((int)(Math.floor(1.0/5*n)),d);
		}
	}
	
	public static void main(String[] args){
		solution2 s2 = new solution2();
		for (int i=1; i<=10; i++){
			System.out.println(s2.g(i,0));
			System.out.println("--------");
		}
	}
}

