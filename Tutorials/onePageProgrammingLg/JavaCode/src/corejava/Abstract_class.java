package corejava;

/*Abstract Fug*/
abstract class Figure{
	int dim1,dim2;
	public Figure(int dim1,int dim2){
		this.dim1=dim1;this.dim2=dim2;
	}
	abstract public void draw();
	abstract double getArea();
}

class Rect extends Figure{
	public Rect(int i,int j){
		super(i,j);
	}
	public void draw(){
		System.out.println("DRAW Rect");
	}
	public double getArea(){
		return dim1 *dim2;
	}
}

class Trang extends Figure{
	public Trang(int i,int j){
		super(i,j);
	}
	public void draw(){
		System.out.println("DRAW Trang");
	}
	public double getArea(){
		return 0.5*dim1 *dim2;
	}
}


public class Abstract_class {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Figure f;
		f = new Rect(10,20);
		f.draw();
		f.getArea();
		
		f = new Trang(10,20);
		f.draw();
		f.getArea();
		
	}

}
