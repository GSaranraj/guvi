import java.util.Scanner;


public class casese {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner i=new Scanner(System.in);
		int a;
		int b;
		a=i.nextInt();
		if (a>1)
		{
			b=a%100;
			System.out.println(b);
		}
		else
		{
			System.out.println(0);
		}
	}

}
