Java Extension Tut
====================
Ch1: Introduction to java.
Ch2: Lexical Issue in Java
Ch3: Object Oriented programming in Java.
Ch4: Exception Handaling in Java
Ch5: I/O in Java
Ch6: Multi-threading in Java.

Ch7: Java Collections.
=================================
  - it's a collection of Interfaces + Implements(classes) + Algorithms
  7.1 Collection of Interfaces
  ------------------------------
    - Collection     >>>> Colection of ele
      - List         >>> Seq of Ele
      - Set          >>> Seq of Uni Ele
         -- Sorted Set >>> Sorted seq of uni ele
      - Queue         >> SPL type of eq
    - Map             >>> collection of <key, value>
        --Sorted Map  >>> Sorted ...
    - Iterator        >>> used to travese a coll
        -- List Iterator  >>> used to traverse list
  -----------------------------------
  7.2: Methods defined
  ----------------------------------
  -- collection :
  add(), addAll(),remoev(obj),remoevAll(col),clean(),contains(obj),containsAll(col),
  equal(obj),HashCode(),size(),toArry(), isEmpty()
  -- List added new func: get(ind),add(ind,obj),indexOf(obj),remove(index),set(inx,obj), subList(start_index,last_index)
  -- Set : no New
  -- Sorted Set : first(),last(),subSet(L,R),tailSet(L)
  -- Queue(FIFO): element() <return head>,offer(obj) <add at last> ,peek()<return head>, poll() <return head and remove> remove() <return head and removed>
  -- Map:         get(k),put(k,v),putAll(map),remove(k),size(),clean(),conatinsKey(),contaisnvalue(),entrySet(),isEmpty(),
  -- SortedMap: All MAP func: + firstKey(),lastKey(),submap(L,R),headMap().tailMap()
  -- Iterator()
    hasnext(),next(),remove()
  -------------------------------------------------------
  7.3 Classes: Actual Implementation of the Interfaces
  --------------------------------------------------------
  AbstrctCollection - Impl colletion
  AbsList           - Im List
  AbsQueue          - Imp Queue
  AbsSequentialList  -Implement lIst
  LInkedlist         -List 
  ArryList            -List Cloneable andSeralizabale
  AbsSet              -Set
  EnumSeyt            -Set
  HashSet             -Set
  PriorityQueue        -Queue
  TreeSet               -Set
  Vector                List+ clone+Serialize
  Stack                 List+ clone+Serialize
  HashTable             List+ clone+Serialize
  ---------------------------------------------------
  7.4 New Method introduced in Class
  ---------------------------------------------------
  Stack: empty(),peek(),push(),pop()
  
  
  ----------------------------------------------------
  7.5 Algorithms
  ---------------------------------------------------
  BinarySerach(L,o),copy(Ls,Ld),disjoint(c1,c2)
  frequency(c,o),reverse(L),shuffle(L,random),swap(L,i1,i2)
  min(),max()
  
  -----------------------------------------------------
  7.6 String Operation in Java
  -----------------------------------------------------
  - 3 Way - > String, StringBuffer and StringBuilder
  - define in java.lang
  - all deceleration are final
  1. Crete a string
    String s = new String();
    char c[]={'a,,'b'}; s= new String(c,0,3);//string(c)
    byte ascii[]={65,66,67}; s= new string(ascii);
    String s= "Dipankar";
  2. Operations
  s.length(),"Hello"+S,s.chatAt(inx),s.indexOf(c),s.lastIndexOf(c),s.subString(l,r)
  s1.concat(s2) ,s1.replace('l','w');s.trim() ,s.toLowerCse(),s.toUpperCse(),
  byte[] getByte() , char[] toCharArray(),s.getChars(l,r,buf,0),
  s1.equals(s2),s1.equalsIgnorecse(s2), s1.startsWith(s2),s1,endsWith(s2), s1.compareTo(s1), s1.regionMatches(boolean ignoreCase, int s_inx, String str2,int str2StartIndex, int numChars) 
  
  - Overwrite toString() in class will use in System.out.println().
  - equls() chck contts but == check same object
  3. String Buffer 
  - It's not a fixed length but growable and mutable. It is Syncronized/
  - Func: length(), capcity(), reverse(), insert(inx,obj),replace(),
  4. StringBuilder
  - Same as String Buf , but NOT sync,- Fast performance, Not not thread safe
  5. Regular Expression
     
    
  










ORM : hibernate Tutorials
===========================
1. Setting up and Installtion :
1.1 Downlod  and install :   http://get.enterprisedb.com/postgresql/postgresql-9.3.4-4-windows-x64.exe
1.2 Downlaod and Import Jars :
http://kaz.dl.sourceforge.net/project/hibernate/hibernate3/3.6.4.Final/hibernate-distribution-3.6.4.Final-dist.zip >> Create a User Lib in Eclipse and put all jar
http://jdbc.postgresql.org/download/postgresql-9.3-1101.jdbc4.jar >> Add this driver as a external lib.
1.3 Create the configuartaion file:
a) Create a conf file hibernate.cfg.xml in src
b) Add the conf indiate the database connection infomation
<hibernate-configuration>
    <session-factory>
        <property name="hibernate.dialect">org.hibernate.dialect.PostgreSQLDialect</property>
        <property name="hibernate.connection.driver_class">org.postgresql.Driver</property>
        <property name="hibernate.connection.username">postgres</property>
        <property name="hibernate.connection.password">dipankar123</property>
        <property name="hibernate.connection.url">jdbc:postgresql://localhost:5432/hibernatedb</property>
        <property name="connection_pool_size">1</property>
        <property name="hbm2ddl.auto">create</property>  <<<<<<<<< Update for keep persitances
        <property name="show_sql">true</property>
        <mapping class="hibernate.code.Student"/>
    </session-factory>
</hibernate-configuration>

c) Login to postgrey swl server and crete a database called "hibernatedb"
d)

2. Writing a Hibernate Application
2.1 Let's Create  a student class
  - Adding Entity Annotated to the class to make it persistences
@Entity
public class Student {
	@Id
	private int rollNo;
	private String name; 
  ...
 }
2.2. Make a Testfile which create object and save these.
      Create Object :Student s1 = new Student(10,"Dipankar");
			Crete a factory: SessionFactory sessionFactory = new Configuration().configure().buildSessionFactory();
			Crete a session:  session = sessionFactory.openSession();
			Start Tractuon : tx = session.beginTransaction();
			Do Database operation :session.save(s1);
			Commit the transation  : tx.commit();
      Rollback if necessary : tx.rollback();
      Close the session : session.close(); 

2.3 Different Annotation to be used Here.
a) Make a Class persistance => 
@Entity
class Studnet
b) Change Name of the Table
@Entity(name= "STUDNET")
public class Student {  
c) Change the name of the column
	@Column(name="STU_NAME")
	private String name;    
d) Another way to change Table name
@Entity
@Table(name="OOO")
public class Student {  
e) Skip a filed to save
	@Transient
	private String name;
f) Primary key auto generated :
	@Id @GeneratedValue(strategy=GenerationType.AUTO)
	private int id;

2.4 Embeded objects

  




