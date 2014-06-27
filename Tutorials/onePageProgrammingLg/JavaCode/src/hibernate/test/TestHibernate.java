package hibernate.test;

import hibernate.code.Student;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;


public class TestHibernate {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		/* Creating two student */
		Student s1 = new Student(10,"Dipankar");
		Student s2 = new Student(20,"Subhankar");

		Transaction tx = null;
		Session session = null;
		try{
			/* Save Objects */
			SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
			session = sessionFactory.openSession();
			tx = session.beginTransaction();
			session.save(s1);
			session.save(s2);
			tx.commit();
			
			/* Retrive the Objects*/
			session = sessionFactory.openSession();
			tx = session.beginTransaction();
			s1= null;
			s1 = (Student) session.get(Student.class, 2);
			System.out.println(s1.getName());
			tx.commit();
			
		}
		catch (HibernateException e) {
	         if (tx!=null) tx.rollback();
	         e.printStackTrace(); 
	      }finally {
	         session.close(); 
	      }

		
		

	}

}
