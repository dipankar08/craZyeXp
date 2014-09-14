/************************
 This bascially contains all functions which is called by C++ func.
 1. We have cretad a Student class.
 2. We have a RJNI test class we basiclly show 4 diff call
 a) Just a cal
 b) pass a String
 c) Pass an Obj
 d) Pass an Obj Arry
 e) reeturn a Obj
 3. Run this application as 
 <javac RJANI.javac > It will give the class file.
 
 *************************/
package Java;

class Student{
private String name;
private int roll;

public Student(){
	name = "Default";
	roll= -1;
	}
public	Student(String name, int roll){
	   this.name = name;
	   this.roll = roll;
	}
	@Override
public String toString() {
		return "Student<name=" + name + ", roll=" + roll + "> ";
	}
  
};


public class RJNI {

	public static void main(String args[]){
		System.out.println("Congrts! This function is called from C++.\n");
	}
	public static void takeString(String in){
		System.out.println("Congrts! We received a String as "+in);
	}
	public static void takeObj(Student s){
		System.out.println("Congrts! We recive an Objects:"+s);
	}
	public static void takeObjArr(Student a[]){
		System.out.println("Congrts! We received an Array of Obs:\n");
		for (Student s: a){
			System.out.println(s);
		}
	}
	public static Student returnObj(){
		System.out.println("Let's Return an Obj");
		return new Student("Diapnkar",100);
	}
}
