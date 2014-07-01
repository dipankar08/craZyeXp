package corejava;

public class Student implements Comparable<Student>{
	private String name;
	private int roll;
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getRoll() {
		return roll;
	}
	public void setRoll(int roll) {
		this.roll = roll;
	}
	@Override
	public String toString() {
		return "Student("+roll+","+name+")";
	}
	public Student( int roll,String name) {
		super();
		this.name = name;
		this.roll = roll;
	}
	/* Allow to detect dupliactes */
	public boolean equals(Object d){
		if(! (d instanceof Student)){
			return false;
		}
		else{
			Student stu=(Student) d;
			return this.roll == stu.roll;
		}
	}
	@Override
	public int hashCode() {
	    return roll;
	}
	
	public int CompareTo(Object o){
		if(o == this){
			return 0;
		}
		else if(!(o instanceof Student)){
			throw new IllegalArgumentException("Apple and Orrange can;t eb comapre!");
		}
		else{
		return this.roll - ((Student)o).roll;	
		}
	}
	@Override
	public int compareTo(Student arg0) {
		return this.roll - arg0.roll;
	}
	/* test the functions Here */
	
	public static void main(String args[])
	{
		Student s = new Student(1,"dipankar");
		System.out.print(s);
		
		Student s1= new Student(2,"Diapnkar123");
		
		System.out.println(s.equals(s1));
	}

}
