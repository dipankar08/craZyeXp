package corejava;
/***************************************
 * 
 * @author Dipankar.Dutta
 *  Topics : Object, Class, Static, Final, Const, Getter , setter, this, method overlaod,cons overload
 ****************************************/

 class Box
{
	/* Instance AVraible */
	private int height,width;
	
	/*Static Variable*/
	static int count;
	
	/*Contractor Overload  */
	public Box(){
		height = width =-1;
		count ++;
	}
	public Box(int i){
		height =width =i;
		count ++;
	}
	public Box(int height, int width) {
		this.height = height;
		this.width = width;
		count ++;
	}
	/*Member function Overload */
	public void  show(){System.out.println("SHOW WITH NO ARGS");	}
	public void  show(int i){System.out.println("SHOW WITH INT ARGS");	}
	public void  show(double i){System.out.println("SHOW WITH DOUBLE ARGS");	}
	public void  show(int i, int j){System.out.println("SHOW WITH TWO INT ARGS");	}
	
	/* Member passing and returing objects */
	public Box AddTwo(Box b1){
		return new Box(this.height+b1.height,this.width+ b1.width);
	}
	/* Setter and Getter */
	public int getHeight() {return height;}
	public void setHeight(int height) {this.height = height;}
	public int getWidth() {	return width;}
	public void setWidth(int width) { this.width = width;}
	
	/* Finalize */
	 protected void finalize(){
	 System.out.println("This Object is now Finalized !");	
	}
	/*Static Variable */
	 static int a =3;
	 static int b;
	/* Static Bolck to initilizae  */
	 static {
		 System.out.println("Static Block is executed to initilize b");
		 b = a*4;
	 }
	 /*Static method can only access Sttic variable*/
	 public void staticX(){
		 System.out.println("I am in Static X");
	 }
	 public void showStatic(){
		 staticX();
		 System.out.println("Static Variable : a="+a+" b= "+b+" Count: "+count);
	 }
	 
	 /* Final Example */
	 final int FILE_SIZE = 400;
	 public void ChangeFinal(){
		 System.out.print("Final Methid Cannot be changed:"+FILE_SIZE);
		 //FILE_SIZE =300; 
		 
	 }
	 
	 
	/*Overload Operators */
	@Override
	public String toString() {
		return "Box(" + height + "," + width + ")";
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (obj == null) return false;
		if (!(obj instanceof Box))
			return false;
		Box other = (Box) obj;
		if ((height != other.height) || (width != other.width))
			return false;
		return true;
	}
		
	
}
 
public class SimpleClassObjectWithStatic {
	public static void main(String[] args) {
		Box b;
		b = new Box(); System.out.println(b);
		b = new Box(10); System.out.println(b); 
		b = new Box(10,30); System.out.println(b);
		
		b.show();b.show(1);b.show(1.0); b.show(1,2);
		b.setHeight(100);b.setWidth(300);System.out.println(b);
		
		b.showStatic();
		
		Box b1 = new Box(10,20);
		Box b2 = new Box(10,20);
		System.out.println("is b1 == b2 ?:"+ (b1 == b2));
		
		
		
		b.finalize();
		
	}


}
