package corejava;

class A{
	int i,j;
	public A(int i, int j){
		System.out.println("A: Contractor called!");
		this.i=i;this.j=j;
	}
	
	public void ShowA(){
		System.out.println("A: SHow"+(i+j));
	}
}

class B extends A{
	int k;
	
	public B(int i,int j,int k){
		super(i,j);
		System.out.println("B: Contractor called!");
		this.k =k;
	}
	public void ShowB(){
		super.ShowA();
		System.out.println("B: SHow sum:"+(i+j+k));
	}
	
}

public class Inheritence {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		A a = new A(1,2);
		B b = new B(10,20,30);
		
		a.ShowA(); b.ShowB(); b.ShowA();


	}

}
