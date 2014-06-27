/**
 * 
 */
package hibernate.code;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Transient;

import org.hibernate.annotations.GenerationTime;

/**
 * @author dipankar.dutta
 *
 */
@Entity
@Table(name="OOO")
public class Student {
	@Id @GeneratedValue(strategy=GenerationType.AUTO)
	private int id;
	private int rollNo;
	private String name;
	
	
	
	public Student(int roll, String name){
		this.rollNo=roll;
		this.name =name;
	}
	public int getRollNo() {
		return rollNo;
	}
	public void setRollNo(int rollNo) {
		this.rollNo = rollNo;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	@Override
	public String toString() {
		return "Student [rollNo=" + rollNo + ", name=" + name + "]";
	}	
};
