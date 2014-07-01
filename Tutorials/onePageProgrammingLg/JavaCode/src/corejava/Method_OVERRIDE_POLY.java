package corejava;
class AA{
	public void show(){System.out.println("I am in A");}
}

class BB extends AA{
	public void show(){System.out.println("I am in B");}
}

class CC extends AA{
	public void show(){System.out.println("I am in C");}
}


public class Method_OVERRIDE_POLY {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		AA a = new AA();
		BB b = new BB();
		CC c = new CC();
		
		a.show();
		b.show();
		c.show();
		
		AA ref;
		ref = a;ref.show();
		ref = b; ref.show();
		ref = c; ref.show();
		

	}

}
