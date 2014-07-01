Java Extension Tut
====================
Ch1: Introduction to java.
Ch2: Lexical Issue in Java


  2.10 Method:
    - Recursion :
       class Fact{
         static int fact(int n) { if (n<=0) return 1; else return n*fact(n-1);}
         }
  - Command Line Argumnets
      - public staic void main(String args[]) <<<<<< This is command line Args as String
          for(int i=0;i<arg.length;i++) SOP(args[i]) 
  - Variable length argumnets
     - It;s as simple passing get(int a[]) { SOP(v.length); for (int x: v){SOP(x);} 
     - calls as => int v[] ={10,20,30}; get(v); 
     - ANOTHER WAY : USE TRIPLE DOT get(int ... v) {...same ..} ; 
     - the variable length argument must be at end: doit(int a, siting b, double ... y){..}
      - This WRING wget(int ... x, int x) or wget2(int ... z, double ... y)
      -RULE : VRS at END. only one VAR at a time
==========================================================
Ch3: Class & Objects: Object Oriented programming in Java
==========================================================
  ------------------------------
  3.1 Basic Class and Objects
  ------------------------------
    3.1.1 Basic Concept
        - Object - Real tiem entity -have state (properties ) and Behavious (method on state)
        - Class : template/blue print that describes the behaviours/states that object of similar type.
        - example : Dog: then its state is - name, breed, color, and the behavior is - barking, wagging, running. Dog is a class and  THE dog of your home is a object
        - Software objects also have a state and behavior. A software object's state is stored in fields and behavior is shown via methods.
        - define a Class in Java : Variables + Methods    
        public class Dog{
        private String name; <<< It's Private, default is public in same class
        private int age;
        public void barking() {};
        }

    3.1.2 Variable :
       1. Instance Variable : Onces per objects
       2. Class /Static Variable : Once per Class
       3. Local Variable : local to method/block 

    3.1.3 Methods : are the function in class
        - Acess the class varible with out a dot.
        - they can take parameter or return value
        - they can be overload by passing multiple papter or diff type with same name: example : test(int), test(int,int), test(double) - but double test(double)
        - Object as a Parameters: boolean equals(Box b){ return this.h == b.height }
        - Object as a Return : Box Incby1(Box b) { return new Box(b.h+1)};
        - Type of Argument passing : 
          1. Call by Value : swap(int i,int j){..} swap(10,15)
          2. call by ref: Crete an object O<i,j> and pass the object swap(object o)
          - Premitive type passed as a call by value but object are always passed by ref. 


    3.1.4 Setter and getter methods - Set or get prvate variable , make access to public

    3.1.5 Contractor : 
        - Initializing the Objects with different way
        - With No Constacter : Java provide default constaer to set everything as null
        - They are same name as class and make it public : public Box(int)
        - Constater can be parametrized
      - They can be overloaded like methods: Box(), Box(int), Box(int,int,int)

    3.1.6 detractors :
        - No delete operator in c++
        - Object destroyed by garbage collector automatically
        - finalize method can be used to cleanup task: protected void finalize(){..}
        - finalize doent called when ob goeses out of scope but execute just before getting gurbage collected So we donot knwo when it will be called.

    3.1.7 This Keyword
        - this ref the the object for which we make a call for a methods
        - used to resolve name like : setWidth(width){ this.width = width;}
        - used to return the same object getObj(Box b) ( return new box(b.h);}
    3.1.8 Objects: those are creted from class
        - Declaration : Just define no mem blocked.: Dog d,d1;
        - Instantiation: Use new word: Dog d= new Dog();
        - Initialization: call to constacter : Dog d = new Dog("LULU",10);
        - Delition - No detete work - java garbae colectio  wil take care.
        - Multile ref of same object might happen
          Box b = new Box(); Box c =b , c and b now point to same box. no NEW() indicate n new obj. defre by b = null;
        
    3.1.9 Accessing class properties:
        - Use Dot operator : d.age or d.setname()..
        - Only public member can be acess
        - Access Static Member by class name :DOG.count or DOG.getCount
    3.1.10 Java Modifier :
        - Access Modifier:
          1. Default / No modifoer - Visible to package.
          2. private - Access by same class method
          3. public - Access to all metthod( same class, other class, other pachage)
          3.Protected- Access to method( SameClassInPkg+OtherClasInPKG+ SUbclass_inotehrpackage)
        - Non-Access Modifier:
          1. Static - Variable  is a variable that one per class
                  - Method can be called without initiation - use only Staic data/method, canot use this or super.
                  - Can be acessable by CLASS.STACTIC
          2. Final  - Like const - Can be initialize only once , ref only one object
                  - However the data pointed by final varaible can be changed
                  - With variables, the final modifier often is used with static to make the constant a class variable.
                  - A final METHOD cannot be overridden by any subclasses.
                  - A final CLASS cannot be inherted.
                  - ex: final int FILE_OPEN = 1;
                  final class F{..} then  class G extends F{..} is wrong
          3. Abstract : 
                  - abstarct METHOD is a method declared with out any implementation.body is missing , must be implent is sub class, thus never be final or static. extented class ,must implement ALL abs method
                  - abstract CLASS contact atleast one abs method.can never initiated. Sole purpose to be extended. Can be abs and final at same time.
          4. Synchronized 
                   - sync METHOD can be acess only one thread at a time
          5. transient 
                   - varaibel not persistance- JVM skip this variable whiel serializaing.
          6. volatile -   
                  - JVM sync the cached copy while same varable is access and modify by multiple thread.
    3.1.11 Nested and Inner class : 
        - class Winthin Anotehr class
        class outer{
        int outer_x =100;
        void test(){ Inner in = new Inner(); in.display();}
        class inner{ void display(){print out_er_x};}
        }
        - Inner class has a direct access to Outter function and data
        - Outer class doent have direct access to inner properies , they have to do it by creteing object of inner and access by that obj.
    3.1.12 Operator Overloading 
  ---------------------------------------------    
  3.2 Inheritances, Polymorphism and Interfaces
  ----------------------------------------------
    3.2.1 Has-A relationship.
    ---------------------------
    3.2.2. IS-A : Inheritances
    ----------------------------
      - crete a Class extending another class.
      - Use extend keyword. It can extend one class at a time.
      ex: Class A {int i, int j} 
          class B extends A {int k;} <<< Have access of i,j
      - Access Rule :
        1. private memeber can't get inherited.
        2. Default and public memeber get inherited.
        3. Protected member in base class gets into protedted in derived calss
      - A Super class variable can ref sub class variable, but those which are dirved only.
        class Box{ int h,w,d;..} 
        class Wbox extend Box{ int waight; ...}
        Box b = new Box(); Wbox wb = new WBox();
        b = wb ;  b.h =>Ok but b.waight=>nOT OK.
      -SUPER: Accessting base info
        1. USE 1: passing parameter to super class .
          - SUPER alwas refer to the immediate super class constarer.
          class Wbox extends Box{ ... Wbox(h,d,w,waight) { super(h,d,w);width= width;}
        2. USE2: Acts like this , but refer immediate parnet class method n var
          class A{int i}
          class B extends A{ int i; 
          void set(i,j) { super.i =i; this.i =j;}
      - Multilevel INheritences
        class A{ int i};
        class B extends A {int j;}
        class C extends B {int k;} <<< Have the info of i,j,k
        
      - How Constacter gettig called for Multilevel
        - It;s from top down. A-->B-->C
      - METHOD OVERRIDING
        - happens when super and sub-class have same func with same prototype
        class A { display(I AM IN A);}
        class B extends A { display(I AM IN B});
        A a; B b;
        a.show() => A
        b.show() => B;
        b.super.show() =>A
        - Overriding ONLY happend if they have same signature
        Rule :
         1. Instance methods can be overridden only if they are inherited by the subclass.
         2. A method declared final cannot be overridden.
         3. A method declared static cannot be overridden but can be re-declared.
         4. If a method cannot be inherited, then it cannot be overridden.(private)
         5. A subclass within the same package as the instance's superclass can override any superclass method that is not declared private or final.
         6. A subclass in a different package can only override the non-final methods declared public or protected.
         7. Constructors cannot be overridden.
      - DYNAMIC METHOD DISPATCH
          - We have base class A
          - B C D are three derived class of A
          - a,b,c,d are the objects of A,B,C,D
          - A r ;//refer of base class
          - r = a; r.show() ==>A
            r= b; r.show() ==> B;
            r=c ; r.show() ==>C
          - r is refer any sub -class at runtime and its func binding at run time only.
          - Support "One interface Multiple Methods"
    -------------------------
    3.2.3 Abstract Class & Interfaces
    -------------------------
      - Ans Abs methods doent ahve any body , but only signature
      - A class habving ATLEAST one abs method call abstract class . It might have other concrete methis.
        - public abstract class A{ show();display();}
      - Abstract class  can't be instantiated. We suppose to create concrete class from abstract class, which implemnet all the abs method. We can crete an ref of Abstract class and point to the obj of concrete class and access the methods.
    - Interfaces 
      - Interfaces are the collection of Abstract methods only. 
      - An concrete class shoud Implement all Abs method of an interface.
      - Interface is not a class, still it like same, but only declare the method we should implement while designing.
      - RULE:
          1. It includes any number of methods
          2. Name of interface is same as .java file name
          3. byte code of an interface in a .class file
          4. you canot instantiate an interface, but crete ref
          5. it doent ahve contrcter 
          6. ALL of the methods in an inetrface are abstract
          7. It doent contact any variable , if appear it must ve static and final both
          8. it can;t be extended but must be implemented.
          9. An interface can extends multile interfaces ( That is a MULtipule inheritences)
          10. When you implement an interface method, it must be declared as public.
          11. If a class includes an interface but does not fully implement the methods defined by that interface, then that class must be declared as abstract.
          12. interface that contains variables that are initialized to the desired values: all are bydefault final.
          interface SharedConstants {
          int NO = 0;
          int YES = 1;
          int MAYBE = 2;
          int LATER = 3;
          int SOON = 4;
          int NEVER = 5;
          }
       - example
       public interface Hello{
       void say_hello(){};
       void get_hello(){};
       public final static DEFIBE =10;
       }
       - Extending interface:
       public interface Sports{..}
       public interface Football extends Sports{..}
       public interface Hockey extends Sports{...}
       public interface Hockey extends Sports, Event{...} //Multiple.
    ---------------
    3.2.4 Packages:
    --------------
        - class is a lower level of abstraction - Grouping of methods
        - package are more upper level abs, Grouping of class
        - Packages are used to prevent naming conflicts, to control access
        - A Package can be defined as a grouping of related types(classes, interfaces, enumerations and annotations ) 
        - Define a class inside a package
          //Hello.java
          package org.hello;  
          class Hello{ static void display()}
        - Compilation cretes the following hirerchy : org/hello/Hello.class
        - Import a Packages and Access
           import org.hello.Hello => display()
           import org.hello.*     => display()
           import org.hello       =>Hello.display()
           import org             =>hello.Hello.dispaly()
           or > org.hello.Hello.display();
        - The name of the package must match the directory structure where the corresponding bytecode resides.
        - To get a Direct Acess please set the class Path such that lookup of class file be set dr.
         $CLASSPATH=/home/jack/java/classes; export CLASSPATH
        -The star form may increase compilation time—especially if you import several large packages. For this reason it is a good idea to explicitly name the classes that you want to use rather than importing whole packages. However, the star form has absolutely no effect on the run-time performance or size of your classes.
        
           
           
        
        
       
       
       
      
      
      
        
        
        
      
      
        
        
      



Ch4: Exception Handling in Java
=================================
Ch5: I/O in Java
=================================
Ch6: Multi-threading in Java
=================================
  6.1 Why Threading ?
    - Myltitasking in two way : Multi processing or Multi threaded
    - Multi tasking thread has less overhead of multit-pocessing 
    - Single threading Process: EVENt loop and polling. have a queue, do the event until queue is empty - problem blocking in nature
    - Multithreading removing this polling or main loop
    - Multithreaded program contains two or more parts that can run concurrently and each part can handle different task
    - LifeCycle [NEW] -> {RUBABLE] <--> [WAITING/TIMELY WAIT/TERMINATED]

    - Thread prority indicate whicg thread to run firtst - two way : preempted and non -preemted.
    - issue : 
        1.Syncronization
        2. Inter thread comminuiction
        3. Deadlock
    - In Java Two way to achive mutithreading
        1. Extend Thread class
        2. Implement Runnable interfaces
  6.2 Threading by impementing runable interfaces
     - 
  6.2 Threading using Extending Thread Class
      - Getting Current Thread : Thread t = Thread.currentThread()
      - t.getName() /t.setName() getting and Setting name
      - t.isAlive() True if it is alive
      - t.join() - caller wait for t to terminated
      - Thread.sleep(sec) - makeing t to sleep to itself
      - Impelment run() to be executed by thread. 
      - t.start() - Will call run() method
      
Ch7: Java Collections.
=================================
  - it's a collection of Interfaces + Implements(classes) + Algorithms
  7.1 Collection of Interfaces
  ------------------------------
    - Collection     >>>> Collection of Elemnets
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
  Vector: Resizeable Array:
  - Vector is Sync but ArryList is NOT!
  - Can iterate vai for loop and Iterator : Merge of Abs List + ARRy list
  - v.size(),v.capacity(),.indexOf(),v.get(idx)
  Stack:
    - Sub clas of vector / Sync
    - Support FIFO
    - empty(),peek(),push(),pop(),search()
  Hash Table/hash map:
    - Both Store <key/Value pair>
    - Similar to HashMap but it sync
    - We nned to implemnet hashCode()and equals()
    - Doent support iterator. To iterator get Keyset or Entry set
    -ops: put(k,v),get(k),keyset(),values(),entrySet()
  ArrayDeque /Queue-
    - Add() - adding at end
    - push() - adding at print
    - remove()/pop() - removing at front
    - removeLast() > remove at last.
    - (add | remove |peek )(fornt|last) : 6 method to do full access  
  Priority Queue :
    - You need to imaplemnet CompareTo() Method in the base class
    - add() => adding at end
    - remove() => getting it from front
    - peek() read the first entry without return it.
    - empty() - Check empty ness
  
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

  




