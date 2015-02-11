
public class solution1 {
	public int d = 0;
	
	public int f(int n){
		d = d+1;
		if (n == 0){
			return 0;
		}else if (n == 1){
			return 1;
		}else{
			return (n*n)+f((int)Math.ceil(n*(3.0/7)));
		}
	}
	
	public static void main(String[] args){
		solution1 s1 = new solution1();
		for (int i=1; i<=10; i++){
			s1.d = 0;
			System.out.println(s1.f(i));
			System.out.println(s1.d);
			System.out.println("--------");
		}
	}
}
