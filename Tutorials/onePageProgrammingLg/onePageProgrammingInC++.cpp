/*
  Name: One Page Progrmming in C++
  Copyright: OnePageProgramming
  Author: Dipankar Dutta
  Date: 07/03/14 22:58
  Description:  
  This is a sequnetila series to keep backup of my Language experience in One Page
  Objectvive:
  - Simple, Brief presise, and easy way to keep the backup of my LG exp.
  - Quick Rampup of any language
  - Quick Serach of any Syntax in Chrome
  - Quick Update and adding more feature and notes easily.
    
Table of Contents:
-----------------------------------------------------------------------------------------------------------
       "One Page Programming in C++"
                                  - by Dipakar Dutta
-----------------------------------------------------------------------------------------------------------
 
      Part I : C++ As a programming language.
      Chaper 1: Introduction of C++
      2.
      3.
____________________________________________________________________________________________________________

0. Intoduction to OOPS
	
	0.1. Softawre Requirements
		- Wow to present reallife entities?
		- S/W with open interface
		- S/w Reusiblity and Extensibility
		- Modules that keep change in future
		- Impove Quality?
		
	0.2. Software Evalution
		- Corerctness
		- Maintanbility
		-Re--use
		-Open neses and Interoperabilty
		-potability
		- Securoty
		-Integritu
		-user friendly
	
	0.3. Layers ib Programming LG
		1/0 -> Machine lag->ASM -> Procedure -> OOPS -> Pattersn
	
	0.4. type of pgramming
		a) top dwn modular :
		b) btn up - structure (POP) -> c, fortran, cobol
	
	0.5. Concpet of OOps
		1. Class - Templtes from whre objects got cretaed. Collection of Daata and func
		that munupulate data
		2. Object - Real timeEntrities
		3. Data Hinding  - data of an obecject can be aceess by only those functions
		4. Encapsulation - Encapulated Diff data and fucntion into a calss Unit
		5. Data Abstraction : Class represtation abstarct the Internal operaton on that data
		Like AddMember () Just tell add a member, but how it add, dupliacte chaes, other complex ops are abstracted
		6.InHeretance - Accure peroperties of anpther clasess - Reusblity
		7. Polimrphim : One name - multile menaing
		- One Operator, Diff operation (based on operand)
		 Operation Overloading
		 Function Overlooaindg 
	 
		8. Dynamic Binding 
		- Func call to module is bined at run time onky
		- Draw() can be bouned citrcle draw or rect-dwar at run time.
		9. Message passing
			Two objet can communicates each other
	
	0.6. Benifits of OOPS
		Inheritence -> Reuseness , Modular design
		Data Hinding -> secure program 
		Interace -> Connect thrigh API
		Upgrads
		Well strcure for large system
	
	0.7. Type of OPPS lang
		1. Object based PL : Encap+hinding + auto inni + cleanup +op over (Ada_
		2. Object Oriented PL = 1+ inh + dynamic bind ( C++, java SmallTalk)
	
	0.8. Application of Oops
		- OO database
		- Realtimr system

1. Introduction to C++
	1.1. What is C++ ?
	 - OOPS
	1.2 : Histroy of c++
	  - Devloped by Bjarne Strouprp AT&T Bell labs 1980
	  - C++ = Simula 67 + C
	  - Superset of C
	  - All C program are C++ program
	1.3 Simple C++ Prgram as Below:
	  - Header file  <iostream>, inclusdes  meaning of cout and <<
	    Old styple is <iostrema.h> new style <iostrema>
	  - name Space cout is the scope of std, so std::cout can be sued only by cout 
	    if we include namespace
	  - Every program start with extcly one main(), it's entrty poit
	  - Comment two way
	      Single line  //
	      Block Comments /* blah  *
	  - Ouput opetator : << printf() is still valid
	  -  C++ main() must return an integer, it coant be void
	  - Variable declaration is anyware.. initially gurbage
	  - cin >> will read input upto ENTER
	  - >> and << operator can be cascaeded.
	
	1.4 Basic strructure of a program :
		a) Same cpp file
		 - Inlcude files
		 - Class defination
		 - member func defination
		 - main program
		b) More Organize
		 - One headre file conatisn the class defination
		 - One C file contains the calss mem func def
		 - One main C file inlcude header and client code.
	
	1.5 Compilation and Execution
		1. Wrire and Exit in Notepad, save with extension .cpp
		2. Compile g ++ hello.cpp - o hello
		for multiple file : g++  x1.cpp y1.cpp -o hello
		3. Run ./hello
2. Program Lexical of C++ 
	2.1 KeyWord in C++
	  - words used in program 
	2.2 Identifier
	  - use define name of variable, functiom arry etc Some rule are dr.
	2.3 Constant 
	   - Fixed vaue throght out the program like 123.. "jello:"
	2.4 Variable : 
	   - Place which hold a value at a time,
	2.5 Data type 
	   - Which kind of data it hold, How to interprect the word, size, and valid opps
	   - 3 Kind of Data type
	       Build in  <int, char , float, double , void >
		   Derived : <arry, func, pointer, ref >
		   Userdeinfe :<strcy, uni class, enum >
	   - Data type modifore
		 Signed, Unsigned, long short to support mutile range of size
	   - Void type used for genertic way
	2.6   Symbolc constant :
	   - const 
	   - enum 
	2.7 Type compatabily
	   sizeof('x') == sizeof(char)
	2.8 declaration and defination of varaible.
	  - Declare anyware 
	   int x <<< declaryion and defintion
	   int x = 0 <<< both
	   int n  = strlen(str) <<< Dynamic initialization
	2.9 Refrenece variable
		- Its an Alias of the actual name
		- If we chage the value of one another also canged
		int total = 100;
		int &sum = total; <<<< & is not a Address of operator
		sum = 150;
		<int & > menas a reference to int
		- pssing a ref variable in a function will efect the actual variable changes
	2.10 Pointer vaiable 
		int x =10;
		int *j = &x;
		*j =50;
		cout <<j;
	2.11 Scope of a Vaiable.
	  - Global valibale > Define function outsied/
	  - Scope inside a function : overwrite global scope
	  - Scope inside a block =>overwrite function scope 
	  - Scope resoltion op always retiunr global value <::m>
3. Operator , Operation and Expression.
4. Control Flow of a program.
5. Function in C++
	5.1 Baic of function
		- Collection of exp which do a defite tasks
		- Syntax is like C
		- function defination => bosy
		- function declaration or prototype 
		- local variable and calling variabe
		- calling a function -> f();
	5.2 Main function()
		- main MUST return an integer
		- Take comamnd line arguments or None
	 	int main(int argc, char *argv[])
	 	or <int main()>
	5.3. Function prototype
		- type func_name (arg_list);
	5.4 Function taking variable length arguments
		- void do(...);
	5.5  Diff way of calling 
		call by value => f(int i, int j);
		call by ref   => f( int &i, int &j);
		call by ptr/addr => f(int *i, int *j);
	5.6 Return a Value/ return a pinter / return a ref
		retur by value int f();
		return a ref int & f();
		return a pointer int * x();	
	5.7 Inlien function
		how to reduce function call overhead ?
		sol 1: Macro
		sol 2: inline function, replace the function call by body
	5.8 Default Arguments
		- Take defualt ar if it is not provifed
		- all default arg must be at end.
	5.9 Const argumnet 
		- Cannot mofify that argumnet at function
	5.10  Function Overloading
	 	- same function name, diff op
	 	- diffrentiate bt arg type and count
	 	- return type can't be distigushed
	 	- Rule :
	 	1. find exact match if possible
	 	2. do type caset
	 	3. if multpile match found return error.
	 	
6. Object Orentation In C++
	6.1 Structure in C++
		- Strct Packing of data of diff type, basically a Templted
		- Limitaion of strt in C
			1. This is not kind of build in , 
			2. doenst define the operation on instract , like o3 =o1 + o2;
			3. Doesnt permit data hiding, can accesable sunging DOT
			4.	Struct keyword still need to use . STUDENT s1, s2 is not OK
		- Struct in C++ is a super set of strct in C
		- c++ extension is like :
		  1. Support both variable and func
		  2. Data hinding by making private ( by default public)
		  3. Starct Name are standalone, no need to say struct Student 
	6.2 Introduction to Class
		1.  Spacifying a class 
		   - Class declaration 
		   - Class function defination
		2.  Basic terminology
		  	- Class memebr - function n varaibel
		  	- Visibility lavel : Private public and protected
		  	- data memebr ( instacce varaible + class variable))
		  	- memebr function
		  	- Combining every thing is called encapulation
		3. Define a Memebr function
			- Indise the class defination
				This is an inline defination
			    just like define, No Scope need to mentions
			- Outside
				<ret> <class_name>::<fuc_name> (<args>)
				void item::setdata(int a,int b)
				{
			  	number =a;
			  	cost =b;
				}
			- membership level to resolve their scope
			- member function can acess private data
		4. Creating objects
			- Actully crete an object - Real memory allocation
			- diff way to do that
			item x;
			item x,y,z;
			class item
			{
			...
			}x,y,x;
		 5. Acssing Class member function
		 	x.getdata();
		 	x.putdata(10,20);
		 	x.cost =10 //INVLID
		 	x.name ="hello" //OK.
	     6. making Outside fiunction as inline.
	        class Box{
	        ...
	        public:
	           void getdata() ; //declaration
	        };
	        inline vois box::getdata() {} <<<<<<<<<<<<<<
	     7. Nesting Memebr function
	       - A member function call another memebr function without DOT
		 8. Private member function
		   - Can not be calseed usng object, only callbed by another member func
		 9. Array with in a Classs
		    - an Arry or a strct can be member of a class,
		    class BOX
		    {
		     char name[10];
		     ..
		    }
		 10. Array of Objects
		    Box b[100]
		 11. Static Member variable
			- This is a class variable, one instace per class
			- initilize to zero, whne calss got created.
			- one copy is share by all instace
			- use class name we can aceess that varaible from outside
			- visible within class but lifetime entire program
			int Box::count ; <<<< This the declaration where me git cretated.
			int item::count = 10 ; << giving vaue otehr than 10
		 12. Static Memeber function:
		    - Can access ONLY to otehr static variable or static funct
		    - can be accessed by Box::show_count();
		 13. Object and functions:
		    - Object can be passed as a function argumnet as well retuen from a function
		      void Bix::addBox(Box b1, Box2)
		     	{
		       	height = b1.height + b2.height 
		   		}
		14. Implicit passing an Object : This pointer
		      - when we call a memebr fuction, one function automatically passes
		      - a.addBox()
		15. frined function
			- A non-mener function doent have acces to the private data
			- Sometiem it;s required - define as a friend
			class Box
			{
			  public:
			  friend void gift_box();
			}
			void gift_box(Box a)
			{
			  cout<< a.name;
			}
			Note that
				a. frind functon is not a class memebr - it's a outside function
				b. it;s not in the scope of class, hence can;t be called via object
				c.  this canot access the memebr variabkdirectly but some DOT operaton
				d. usually it has the object an Arguments
			- Forwoard celaration might required someware
		16. Return a objects
		    - just like returning a dtatype   	
				 
		17. Memory Allcation Rule :
		 	- When we define a class , the memoty for Static memebr, memebr function got cretaed.
			- Object cretaing memeber object varaible(instancevariable) are got created.
		18. Varaible Type :
		    1. Local variable
			2. Class variable - Static in nature
			3. Instance Variable.
			4. Global variable 
		19.	Const memebr function
		   void const_fun() const;
		   -- It cannot cahnge any object data
		19. Const Objects
		    const Box b(1,20)
		    // Set value will not change the value of box
		20. Pointers
			1. Pointer to object : Araaw operator access variable
			Box b1;
			Box *bptr= &b1;
			bptr->fun();
			2. Pointer to the memebr of a calss
			int Box::*hp = &Box::height; 
			Box b1;
			count >>&(b.height) >> b.hp ;BOTH are same
			cout >> b.height >> b.*hp >> bptr->hight>>bptr->*hp; //Both same
		21. Local Classes
		   	- define a class insdie a function Like
		   	void test(int a)
		   	{
			   	 ...
			   	class stu
			   	{
				   ...
			   	   ...
			   	}
			   	..
			   	student s1(a);// Objects
			}
		22. Constracter of a Class
			- Spacial member function to initilize the objects
			- Name same as class name
			- Automatically invoked when object got cretaed.
			- Donegnt have any return type, not even VOID
			- can not be inherited,
			- Like member function, it can be overlaoded, default args
			- It cannot be virtual
			Type of contractor
			1. Default - You wrote or compiler prives
			   void box() { ...}
			2. parameterrized contracter
			    box(int h, int w); <=== box(1,2);
			      can be called by two way 
			      Explict Box b= box(10,20);
			      Implicit Box b(10,20);
			3. Contrcteor overloaded : Multiple contractor
			   Box() { h =0;w=0;}
			   Box(int i) { h = w =i;}
			   box(int i,j) {h =i,w =j;}
			4. Constrator with default Argument
			 Box(int h =10, int w =10) 
			 Call : Box b(),b(1),b(1,2)
			5. Copy Constrator
			 - Box(Box &b)
			 { h = b.h, w = b.w;}
			 - They pass the object by referees,can not be pass by value
			 - Alsoo call copy initilization
			 like 
			 Box b(1,2);
			 Box b2 = b1 == Box b2(b1)
			 Note Box b1,b2 ; b1= b2 will not call copy contsrcter, but need a overload
			 - If no copy contr, compiler suffiles it
			 6. Dynamic Contracter
			 Say a class contains a pointer to string : char *name.
			 basied on the passing length of String we allocate the memory and do the stuff.
		23. Destructors
			- Destrct a memebr when not requited.
			- Same as contrractor biut  ~Box() { //Do soem relase }	
			- Delete the allocated mem using new or close fd.
			- call implecily when object goes out of scope
			- Calling sequences
		24. Function Overloading
			-Just like constaror overloading..
			-having same function name , but diff function argument with diff type
			- return type diff can't make func overloading
		25. Operator Overloading
			- Adding spacial meaning to the operator
			- Cant be overlaoded : .| .* :: sizeof() , ;?
			- two way doing ops overhead
			- Basic Syntax:
			ret classname::operator <op>(arglist)
			{  
			  ..
			}
			1. Unary function Overload
				- mem func : vector operator -();
					- Converstion -v1 ==> v1.operator-();
				- friend: friend vector operator -(vector);
					- Converstion -v1 ==> operator-(v1);
				- First argument pass by the object
						
			2. binary ops
			    - mem func : vector operator +(vector);
			    	- Converstion v1 =v2+  v3  ==> v1 = v2.operator+(v2);
			    - friend : friend vector operator +( vector, vector);
			    	- Converstion  ==> v1 = operator+(v1+v2);
			3. Operation with Non Opject  v = v + 3
			    - mem func : vector operator +(int );
			    	- Converstion v1 =v2+ 3  ==> v1 = v2.operator+(3);
			    - friend : friend vector operator +( vector, int);
			    	- Converstion  ==> v1 = operator+(v1,3);
			4. Operation with Non Opject  v = 3 + 4
			    - mem func :  Not Possabile as left side is not an object
			    - friend : friend vector operator +( int, vecttor);
			    	- Converstion  ==> v1 = operator+(3,v1);
			5. We can also over laod istream and ostream operator as well
			    - if we use memebr function it would be like v1 >> cin or v1>> out
			    - But use friend as we need to pass ci and cout as first argument 
			    	this cin >> v1 or cout << v1 would work properly
			6. We can implement all string related opeation using this operator like
			   = + ,  == , != and <= , >- etc.
			7. In same way, you can over laod ++, -- etc.[],() etc
	6.3. Inheritence in C++
		- getting the property of  parent calss
		- parent/ super class
		- child / sub / derived class
		- Modifer basically indicates how we are inhereting the classess.
		- 3 Kind of Modifer ( Mode of derivation)
		1. privatly Inheriteted : Public of base become private of derive 
		2. publicly inherited: Public of base become public of derived, protected become protected
		3. protected : Protected and public become the protected in derived
		4.default :
		5. Private memner of base can't be derived.
		- Type of Inheritences
		1. Single Inheritences
			class B
			{  private:
			   int a;
			   protected:
			   int b
			   public:
			   int c;
			}
			Class D1 : private B << All protected and public become private 
			{ 
			  private:
			  int a1;
			  protected:
			  int b1;
			  public : 
			  int c1; 
			}
			Class D2 : protected B << All protected and public become protected 
			{ 
			  private:
			  int a1;
			  protected:
			  int b1;
			  public : 
			  int c1; 
			}
			Class D3 : public B << All proteced  and public become as it is 
			{ 
			  private:
			  int a1;
			  protected:
			  int b1;
			  public : 
			  int c1; 
			}
			- Here there is issue called overwriding the function and objects
		2. Multiple Inheritences:
		  We have a base class B1, B2 and B3, and D is deriving from every one
		  Class D1: public B1, public B2, private B3
		  {
		  ...
		  }
		  - There is a change of abmiguity , which is resolve by Scope Resolution ops.
		3.Multi level inheritences
		Let A be the base calsss, Class B inherited A and Class C inherited B, Which is basically a multi level
		Class A {..};
		class B: public A {...};
		class C: public B {...}; 
		- Here is a issue in which order constarcter are getting called.
		4. Hybrid Inheritences
		Case 1 : 
			- Student base class
			- Arts Engg and Medical inherites Students
			- Mech, civil, Elec inherite Engg.
		Case 2: 
			- Account is the Base class
			- Saveing, Fixed depot, Cutteent Account inherit Account
			- Short-tern, mid-term , long term inherite Fixed-deposit Account
		Case 3:
			- Sutudent is a base class
			- Exam inhettes test
			- Sport is another class inherites Student
			- Result is inherited both Exam an Sport
		Case 4:
			- We have GP base class
			- Parent1, and Parent 2 are two drive class of GP
			- Child inherte from Parent1 and Parent 2 ( Multiple inheritences)
		Issues:
			1. Child should get one and only copy from parent1 or parnet 2.
			solved by virtual base Class
	6.4 Issues in Inheritances
	 	a) 	Method Overwritten in Single Inheritences
		 	class A { ..} --> display()
		 	class B: public A {..}; --> Dispaly
		 	B b ;
		 	b.display() -->Calls B's display
		 	b.A::display() -> calls A's Dispaly
		 	b.B::display() ->call's B's display
	 	b) Method Amboguity in Multople Inheritances
	 		class B1 and B2 both nas a dispaly() functions
	 		Class D: public B1, public B2{..}; also has diaply function.
	 		void D::display()
	 		{ B1::display() ;
	 		 B2:: display();
	 	    } 
	 	c) Order of calling the constarcter in Multivel inheritences
			We have a Class Hirerchy as A ->B->C 
			then Conster calling sequnecs will be A->B->C
			Destarcter calling sequnece is A->B->C
	 	d) Virtual base class to get only one copy 
			B1,B2 inherits A and C inherits B1,B2. 
			Only one copy of A will be get by C. 
			Sol: inhert A from B1 and B2 virtually
			Class A {..};
			class B1:virtual public A{..};
			class B2: virtual public A{...};
			class C: public B1, public B2{..};
		e) passing parameters while inheritences
			tWo wau to do that.
			- Calling base Contracter from derived consstracter
			class B1
			{ int i,j;
			  punlic :
			    B1(int i,int j){..}
			..
		    }
		    class B2{..};
		    class D: public B1,public B2 <<< this order matters
		    {
		      int e,f;
		      punlic :
		        B(int a,b,c,d,e,f):B1(a,b),B2(c,d) <<<< this order doesnt matter
		        { ..}        
		    }
		    - Inilitilztion List
		    Class B1
		    {
		      int a,b;
		      public:
		        B1(int i, int j):a(i),b(2*j) {..} >>>> a= i;b =2j
		        >>>> Basically do Order of evalution as the order of initilization list
			}
			Class D,publicB1, public B2
			{
			  int e,f;
			  public:
			  D(a,b,c,d,e,f):B1(a,b),B2(c,d),e(e),f(f) { };
			}
	6.5 Exposing Has -A relationship: Composition Aggrigation or nesting the classes
		- Another Way to reuse code.
		- A class conats the objects of another class
		- Indicate a Has-A relationship
		- Example
		Class Empyloyee
		{
		private :
		string firstname;
		string lastname;
		Date birthdate;  <<<<<<<< Another Object of Another class
		Date hireDate;
		}
	
	6.6  Nesting class
	6.7 Poly morhism.
		6.7.1  This pointer
			- Opinter to itself.
			class A
			{ int i;
			  public:
			  A(int i)
			    {  this->i =i; }
			  A Compare_And_return( A & a)  <<<<< Compare two objects
			  {
			     if(a.i > i) return a;
			     else return *this;
			  }
			  A operator ++()  <<< PreIncrement 
			  {
			     this->i ++;
			     return *this;	     
			  }
			  A operator ++()  <<< PostIncrement 
			  {  
			     A temp = *this;
			     this->i ++;
			     return temp;     
			  }
			  
			}
		
		6.7.2 Polimorphisma.
			- Fundtion call - Early binding or stantic linking compile time binding
				class A
				{
				show();
				}
				Class B : public class A
				{ show();
				}
				Main()
				{
				 A a; B b;
				 a.show() ; <=---nCompile time
				 b.show() ; <<<<<< Comple time
				 b.A::show() <<-- Compile time too.
				}
			- Late binding or run time binding
			- Pointer to Object
				 A a, *p;
				 p =&a;
				 a.show() == p->show(); ==(*p).show()
				 A b[10];
				 p = b ; <==== First object
				 (p+3)->show() <<< call for 3rd objects
			- Pointer to Base class, can also point to drived class objects;
			A a, *aptr;
			B b, *bptr;
			
			aptr = &a;
			aptr->show() =>call ShowA();
			aptr->a =10 //Will Work 
			
			aptr  &b;
			aptr->show() ==> Still Call ShowA() ; <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			((B *)aptr)->Show()  => Now it can show B()s
			aptr->b = 10 ; Not work as it is not define in B
			
			bptr = &b;
			bptr ->b =10 ; WORK
			bptr->show() //Works
			
			(A *)bpr ->a = 400 Work.
			(A*) bptr->show() ; A's Show...
			
			- Qn How we can do it without type case ?
		    	 define the function in base class as virtual
		    	 class A {
		    	  virtual void show() {...}
		    	}
		    -Polimorohims Example With Virtual function, pointer to base class can call overwrite func in derived calss without type casee
		    lead to a run time polymorphism.
		    - Pure Virtual Function
		      // Do nothing
		      virtual void display () =0;
		      MUST Required a derived class
	
	6.8 Interface and Abstract class in C++	 
		
7. C++ I/O
   7.1 Console Input Output
   7.2 File Input Output
   		1. 3 main lib
	   	 ofstream	-output file stream and is used to create files and to write 
		 ifstream	- input file stream and is used to read information from files.
		 fstream	- file stream generally :both ofstream and ifstream, al ops
		 1.3 File Operation:
		 a. Open a file. void open(const char *filename, ios::openmode mode);
		 Mode : 
		 ios::app	Append mode. All output to that file to be appended to the end.
		 ios::ate	Open a file for output and move the read/write control to the end of the file.
         ios::in	Open a file for reading.
         ios::out	Open a file for writing.
         ios::trunc	If the file already exists, its contents will be truncated before opening the file.
		 fstream  afile; afile.open("file.dat", ios::out | ios::in ); << Read and Write
		 ofstream outfile; outfile.open("file.dat", ios::out | ios::trunc ); << Write and Truc if exist
		 b) close a file : Do a auto close , best practice void close();
		 c) Reading a file : >>,g
		 d) Writing a file : <<,
		 	- >> and << acts like as cout or cin
		 	- fin.get() and fout.put('c') puts a single ch
		 	- read() and write() for binary data
		 	- Reading and Write objects 
			   file.write((char*) &student1,sizeof(student1));
			   file.read((char*) &student1, sizeof(studnet1)); 
			 - Read and write line by line
			   	fin.getline(data,100); // Saves the line in STRING.
			   	
		 	
		 e) Changing file pointer: 
		 	fileObject.seekg( n );>>  position to the nth byte of fileObject (assumes ios::beg)
		 	fileObject.seekg( n, ios::cur );  position n bytes forward in fileObject
		 	fileObject.seekg( - n, ios::cur );  position n bytes backword in fileObject
			fileObject.seekg( n, ios::end )=>  position n bytes back from end of fileObject
			fileObject.seekg( 0, ios::end ); > position at end of fileObject
			fout.seekp(..) Same for outputing.
			fin.tellg() > tell the pinter of in
			fout.tellp() > tell the pointer for out
		g) Detecting end : fin.eof() !=0
		

		 
8. C++ Exception handaling
10. C++ Generic Programming : Templates
	10.1 Why Templtes ?
		- Provide Genric Class and Functions
		- We can build a class / function shich can be used for all datatype
		- No two function do the same thing for int or float
		- It's kind of macro or just like temaplte , which can generate many actual function
		- We want to devlop to stack, one for integer and another for float, only type difeer body are same
		  In this case Templte would be help ful, It make type indipendent programming like python
	10.2 Function Templates
		10.2.1 Simple function Template
			template <class T>  <<<< This indiactes we want to use type T
			T const& Max (T const& a, T const& b) 
			{ 
		    		return a < b ? b:a;  <<< Return Maximum vaue of any two type.
			} 
		10.2.2 FUnction Template with multiple 
			template <class T1, class T2>
			void display(T1 y,T2 y)
			{ cout <<x <<" " <<y;
			}
		10.2.3 Overloading function Templates
			Say we have 
			template<Class T>
			void display(Tx ){..};
			
			void display(int x){. ..}
			Rule
			1. call the Explict func if they have a match >> display(10) -> call exp
			2. call tempalte function if doent have a orinary function matches.
			3. return error
		
		 
	10.3 Class tempaltes
		10.3.1 Stack Tepplate Classs
			template <class T> <<<<<<<<< This indicate the next class is a tempalte and use type T
			class ABC
			{
			  T i;
			  public:
			  void set( T i);
			  T get();
		    };
		    template <class T>  <<<<<<<<<  We have use this for all mem func defination
		    void ABC<T>::set(T i) { this.i =i;} <<<<< Note that class name is ABC<T>
		    
		    template <class T>  <<<<<<<<<  We have use this for all mem func defination
		    T ABC<T>::get() { return i;} <<<<< Note that class name is ABC<T>
		 
		    - Instentiate Like this:
			ABC<int> int_type; <<<< Create  atrack for integer operation.
			ABC<float> f_type; <<<< Create for float ops. etc..
			int_type.set(1);
			int_type.get();
		
	    10.3.2. Class Templete with Many parametres
			template <class T1,class T2>
			class Test
			{ T1 a;
			  T2 b;
			  public:
			  void set(T1 x, T2 y){ a=x;b=y;}
			};
			- Instentiation:
			Test<int,float> t1;
			t1.set(10,10.4);
	    
	    10.3.3 Class Tempaltes with mixed nintype and typed.
	    tempalte <class T, int size>
	    class array
	    {
	       T a[size]; <<<<<<<<<<, this size is passed by the tempaltes
	       ...
		}
		Ins:
		array<int, 10> a1; <<< Create an arry of 10 integers.
		size acts as an argumnet in the template class
11. C++ STL and Algorithms
	11.1 Structure of Standard templete lib.
		- C++ provides a rich collection of useful data structure and algo
		- It support all kind of Ds like heap, list, stack queue etc.
		- it's the part of std name space
		- It's basically made by 3 components
			1. Containes - the objcets wich store the data
			2. Algorithms - function to process/ manupulate data
			3. Iteration - pointer to elemnts in the container, which iterate over the data 
	11.2  Container : 3type of
			1. Sequence Containe - ORDERED Colletion of ITEM
				- Vector - Dynamic Array - Insert/Detete at Back - Random Access
				- list	 - double Linkedist - insert-del anywhr   - Bidic Access
				- deque  - DeQueue Arry  - Insert/Del AnyEND	  - Random Aceess
			2. Assciate Container - Sorted collection -Support efficient lookpup by Key
				- Set 	    -StoreUnique Ele  -  Rapid lookup		  - Bi-Access
				- multiset  - Set with Dupliactes Rapid lookup		- Bi aceess
				- map 		- one Key-one Value Pair Rapid lookup	-Bi Aceess
				- multimap 	- OneKey-ManyValue	Lookup				-Bi Access
			3. Derived Continer - Really useful but drived.
				- Stack 	FIFO   No Iterator
				- queue 	LIFO 	No iterator
				- Pririty Queue	 - HEAP 	No Iterator
	11.3 Iterator 
		- Itarte over container objects to get the items
		- Why they iterate ?
			1. Input Iterator - read only can't write or modify
			2. Output Iterator - Write into colections
		- How they Iterate ?
			1. Fwd Iterator - Ierate over single linkedlist one direction Only :itr ++;
			2. Bi-dirctinal - both side travset, incremt and decement support : itr++ & itr --;
			3. Random Access - RandomJump to any loc : it+=10 ;
	11.4 Algorithms 
	    - Algorthims to manupulate objects Some Aldo as listed.
	    1. find()
	    2. sort()
	    3. reverse()
	    4. transform()
	11.5 String Class in C
		- Initiantiation:
		   string s ="Dipankat"
		   string s("dipankar");
		   string s; s="dipankar";
		   string s(s1);
		   string s(100,'a') //100 a's
		   
		- Acessing chrater
			=> s[i] =>
			=> s.at(i) =>
			=> string::const_iterator it = s.begin() and a loop. cout <<*it
		- basic properties 
		    => s.length()
		    => s.size()
		    => s.capacity()
		    => s.max_size()
		    => s.empty()
		- Basic Ops
			=> Concat =>s3 =s1+ s3 OR s1.append(s2)
		-   => Substr : s1.find("dip")  or s1.find_first_of('a') or s1.find_last_of('a') : return index
		    => Trancating : s1.erage(10,15) Or s1.erage(it) 
		    => Reversal : revserse(s.begin(),s.end())
		    => Transform: transform(s.begin(),s.end(),s.begin(), toupper);

12. C++ Advance Topics I : Multithreading
12.1 Basic Concept 
	- Multithreading is a specialized form of multitasking
	- multitasking is the feature that allows your computer to run two or more programs concurrently. 
	- Process-based multitasking handles the concurrent execution of programs.
	- Thread-based multitasking deals with the concurrent execution of pieces of the same program.
	- A multithreaded program contains two or more parts that can run concurrently
	- We are using Linux OS ,multi-threaded C++ program using POSIX or pthread
12.2 Pthread Library use
	- #include <pthread.h>
	- Cretaing a thread
		* pthread_create (ref to Ptrread_object, attributes, start_routine_or_code_to execute, arg_list)
		* int pthread_create(pthread_t*, const pthread_attr_t*, void* (*)(void*), void*)
	- Terminating a thread
		* pthread_exit (status) => Terminate a Thread
	- Block the calling thread iuntil spacofied thread terminate
		* pthread_join (threadid, status) =>int pthread_join(pthread_t, void**)
	-  Detach a treaded and Let's them work indipendently , never wait for join
		* pthread_detach (threadid) 
12.3 Issue and Resolution of thread operation.	
    12.3.1 Thread syncronization with Lockinga nd Unlocking
    - Create a Lock
    	pthread_mutex_t lock_x;
    	int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *mutexattr);
    - Locking and unlocking 
    	int pthread_mutex_lock(pthread_mutex_t *mutex);
		int pthread_mutex_trylock(pthread_mutex_t *mutex);
		int pthread_mutex_unlock(pthread_mutex_t *mutex);
	12.3.2 Thread Syncronization usig wait and Signal Opeartion
		- Sipport Conditinal Locking mechnisam
		int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
		int pthread_cond_signal(pthread_cond_t *cond);
		int pthread_cond_broadcast(pthread_cond_t *cond);
		- pthread_cond_wait() puts the current thread to sleep. It requires a mutex of the associated shared resource value it is waiting on.
		- pthread_cond_signal() signals one thread out of the possibly many sleeping threads to wakeup.
		- pthread_cond_broadcast() signals all threads waiting on the cond condition variable to wakeup. 
		
		- Create conditial lock : pthread_cond_t sig_consumer
		- Sleep a thread for an event : pthread_cond_wait(&sig_consumer, &lock);
		- Wake up thread : pthread_cond_signal(&sig_consumer);
	12.3.3  Inter thread/Process comminication
		- Number of way to do that
		a. Using shareed memory
		b. Using message passing ( Called Message Queue)
		
12. C++ Advance Topics II : Signal Handaling
	- signal are the interupt from OS to process
	- we have sumner of signal in C/C++ ins <csignal>
	- Example
	SIGABRT	Abnormal termination of the program, such as a call to abort
	SIGFPE	An erroneous arithmetic operation, such as a divide by zero or an operation resulting in overflow.
	SIGILL	Detection of an illegal instruction
	SIGINT	Receipt of an interactive attention signal.
	SIGSEGV	An invalid access to storage.
	SIGTERM	A termination request sent to the program.
	- Catch an single using a handaler 
	void (*signal (int sig_number_to_be_handle, void (*hanalder_fun_to_be_called)(int sig_number)))(int); 
	Exampel :
	void sighand(int no)
	{
	  cout <<" interrupt signal: "<<no<<"received\n";
	}
	int main()
	{
	  while(1){
	   signal(SIGINT,sighand); <<<<<<< Register a handaler
	   sleep(1);
	  }
	}		
	- programically Raise a signal;
	int raise (signal sig);
	int main()
	{
	  while(1){
	   signal(SIGINT,sighand);
	   signal(SIGSEGV,sighand);
	   sleep(1);
	   raise(SIGINT);
	   raise(SIGSEGV);
	  }
	}
12. C++ Advance Topics III : Name Spaces
	- A namespace allow to use same name for diff lib. sing namespace, you can define the context in which names are defined. In essence, a namespace defines a scope.
	1. Declaring and Accessing name space
	- We have two namespave but they have same func, called specifc one by using scope-reolusion op
	namespace aaa{
	  void display() {cout<<"Inside AAA\n";}
	}
	namespace bbb{
	  void display() { cout <<" Inside BBB\n";}
	}
	int main()
	{
	  aaa::display();
	  bbb::display();
	}
	2. avoid  aaa:: again by usnig <using namespace aaa;>
	using namespace aaa;
	dispaly() >>> AAA 
	aaa::dispaly() == dispaly()
	3. Nesting namespace
		namespace ccc{
	  void display(){ cout<<"inside CCC\n";}
	  namespace ddd{
	    void display(){ { cout<<"inside CCC::DDD\n";}}
	  }
	}
	using namespace ccc ==> Call CCC
	using namespace ccc::ddd;==> call CCC::DDD
____________________________________________________________________________________________________________
*/
#include<string.h>
using namespace std;
/*******************************************************************************
* Chapter 0: Intodcution  to Object Oriented Programming
* Topics :
* KeyNotes:

*******************************************************************************/

/*******************************************************************************
* Chapter 1: Intodcution to C++
* Topics :
* KeyNotes:

********************************************************************************/
#include <iostream>

using namespace std;
#if 0
int main()
{}  
    /* Printng Hello World. */
    
	//std::cout << "hello World"<<std::endl;
	cout <<"hello World"<<endl;
	
	float n1,n2,sum,avg;
	cin >>n1;
	cin >>n2;
	//cin >>n1>>n2;
	
	sum = n1 +n2;
	avg = sum /2.0;
	cout <<"N1: "<<n1<<" n2: "<<n2<<" Sum : "<<sum<<" Avg : "<<avg;
	
	return 0;
}
#endif




/*******************************************************************************
* Chapter 2: Lexical of C++ 
* Topics :
* KeyNotes:

*******************************************************************************/
#if 0
void swap1(int i, int j)
{
	i = i + j;
	j = i - j;
	j = i - j;
}
void swap2(int & i, int &j)
{
	i = i + j;
	j = i - j;
	i = i - j;
}

void swap3(int * i, int *j)
{
	*i = *i + *j;
	*j = *i - *j;
	*i = *i - *j;
}
int m = 1;
int main()
{
	int total =10;
	int &sum = total;
	sum =50;
	cout << total<<endl;
	
	// diff bet call by value, call by ref, call by address
	int i=10,j=20;
	
	swap1(i,j);	
	cout <<i<<" "<<j<<endl;
	
	swap2(i,j);
	cout <<i<<" "<<j<<endl;
	
	swap3(&i,&j);
	cout <<i<<" "<<j<<endl;
	
	/* Scope Of variable */
	cout <<"m0: "<<m;
	int m =2;
	cout <<"m1: "<<m;
	{
		int m =3;
		{}             // <<<<<<<<<< Start a new scop
			cout <<" m2: "<<m;
			int m =4;
			int k =3;
			cout <<" m3:"<<m;
			cout <<" m3+:"<<::m;
		}
		cout <<" m4:"<<m;
		//count <<k; <<<<<,, Not in scope
	}
	cout <<" m5: "<<m;
	return 0;
}

#endif


/*******************************************************************************
* Chapter 3: Operator , Operation and Expression.
* Topics :
* KeyNotes:


********************************************************************************/
/*******************************************************************************
* Chapter 4: Control Flow of a program. 
* Topics :
* KeyNotes:

********************************************************************************/
/*******************************************************************************
* Chapter 5: Functions in C++ 
* Topics :
* KeyNotes:
********************************************************************************/
#if 0
void fuc_over(){cout<<"No arg"<<endl;}
void fuc_over(int i){cout<<"INT arg"<<endl;}
void fuc_over(int i, int j){cout<<"INT INT arg"<<endl;}
void fuc_over(int i, double j){cout<<"INT FLOAR arg"<<endl;}
void fuc_over(double i, int j){cout<<"FLOAT INT arg"<<endl;}
void fuc_over(double i, double j){cout<<"FLOAT FLOAT arg"<<endl;}

void default_arg(int i=1,int j =2, int k =3)
{
	cout <<i<<j<<k<<endl;
}

void cost_arg(const int x)
{
 //	x=20; Will not workd as x is readonly */
}
int &max(int &x, int &y)
{
	if (x>y)
	  return x;
	else
	 return y;
}
inline float mult(float x, float y)
{
	return (x*y);
}
void test_ch5()
{}
    /* Return by ref */
	int x=10, y= 20;
	max(x,y) = -1;
	cout << x << y <<endl;
	
	/*inline function */
	cout << mult(10,20)<<endl;
	
	/* default arg */
	default_arg();
	default_arg(10);
	default_arg(10,20);
	default_arg(10,20,30);
	
	/*const arg */
	cost_arg(10);
	
	/* func ovreloading*/
	fuc_over();
	fuc_over(1);
	fuc_over(1,1);
	fuc_over(1,1.0);
	fuc_over(1.0,1);
	fuc_over(1.0,1.0);

}
#endif
/*******************************************************************************
* Chapter 6: Class and objects  PART -I
* Topics :
* KeyNotes:
********************************************************************************/
#if 0
class Box
{
	int height; //<<<<<<,, Private by defualt
	int width;
	char name[10];
	static int count; //static declaration
	
	void private_show()
	{
		cout << "This is a private Memebr function";
	}
	
	public:
		int z;
		Box()
		{
			cout<<"Default Cons"<<endl;
			height =0;width =0;
		}
		Box(int i)
		{
			cout<<"Default Cons"<<endl;
			height =i; width =i;
		}
		Box(int i, int j)
		{
			cout<<"Default Cons"<<endl;
			height =i;width =j;
		}
		/*Box( Box & i)
		{
			cout<<"Default Cons"<<endl;
			height = i.height; width = i.width;
		}*/
		~ Box()
		{
		//	cout<<"Destractor called"<<endl;
			
		}
		void setdata(int h, int w);// only declaration
		//Inline 
		void getdata()
		{
			cout <<"height: "<<height<<" Width: "<<width <<endl;
		}
		void show()
		{
			private_show();/*nested call without do operator*/
		}
		void setName( char n[])
		{
			strcpy(name,n);
			cout <<"name become: "<<name <<endl;
		}
		static void getCount()
		{
			cout<<"Static Count is: "<<count<<endl;
			//count <<height; Canpt access
		}
		
		void addBox(Box b1, Box b2)
		{
			height = b1.height + b2.height;
			width = b1.width +b2.width;
		}
		
		friend Box DoubleBox(Box b);
		void const_fun() const;
		
		/* Operator Overloading */
		void operator-()
		{
			height = -height;
			width = -width;
		} 
		Box operator+(Box & b)
		{
			return Box(height+b.height,width+b.width);
		}
		friend void operator~(Box &);
		friend Box operator-(Box,Box);
		friend bool operator==(Box,Box);
		friend Box operator +(Box,int);
		friend Box operator +(int,Box);
		friend istream & operator >> (istream &i, Box &b);
		friend ostream & operator << (ostream &i, Box b);
}; 

int Box::count = 10;
/* Outside defination */
void Box::setdata(int h, int w)
{
	height = h;
	width =  w;
	count ++;
}
void Box::const_fun() const
{
	// height =10; //ERROR
}

/* Frined functions */
void operator~(Box &b)
{
	b.height = - b.height;
	b.width = - b.width;

}
Box operator-(Box b1,Box b2 )
{
   return Box(b1.height + b2.height,b1.width+b2.width);	
}

bool operator==(Box b1,Box b2)
{
	if (b1.height == b2.height && b1.width == b2.width)
	  return true;
	else
	  return false;
}
Box operator +(Box b,int i){
	return Box(b.height+i,b.width +i);
}
Box operator +(int i,Box b){
	return Box(b.height+i,b.width +i);
}

istream & operator >> (istream &i, Box &b){
	i >>b.height;
	i >> b.width;
	return i;
}
ostream & operator << (ostream &i, Box b){
	i << "Width: "<<b.width <<" Height: "<<b.height <<endl;
	return i;
}

		
/* friends */
Box DoubleBox(Box b)
{
	Box newb;
	newb.height = b.height*2;
	newb.width = b.width*2;
	return newb;
}


void test()
{
	Box b; // Cretaing objects
	
	cout<< "Priniting Box "<<endl;
	b.setdata(10,20);
	b.getdata();
	//b.x = 10; >>>> Error : no memebr as x
	b.show();
	//b.private_show(); >>>.. canot access
	
	b.setName("myBox");
	
	Box bList[10];
	for(int i=0;i<10;i++)
	{
		bList[i].setdata(i,i+1);
		bList[i].getdata();
	}
	
	/* Static*/
	Box::getCount();
	
	/*Passing Ob */
	Box b1,b2,b3;
	b1.setdata(10,20);
	b2.setdata(20,30);
	b3.addBox(b1,b2);
	b3.getdata();
	
	/* Friend function and return Objects */
	Box b4 = DoubleBox(b1);
	b4.getdata();
	
	/*const func */
	b4.const_fun();
	
	/* Pinters */
	Box *bptr = &b4;
	bptr->getdata();
	
	int Box::*zp = &Box::z;
	b4.z =10;
	cout<<"Address of member: "<< (b4.z) << " " << b4.*zp<<" "<<bptr->z<<" "<< bptr->*zp<<endl;
	
	/* Constractro */
	Box a1; a1.getdata();
	Box a2(1); a2.getdata();
	Box a3(1,3);a3.getdata();
	Box a4(a3);a4.getdata();
	
	/* ops Overlaod */
	cout <<endl<<endl;
	Box x1 = Box(2,3);
	Box x2 = Box(4,5);
	x1.getdata();
	-x1;
	x1.getdata();
	~x1;
	x1.getdata();
	
	cout << (x1==x2);

    
    cout << (x1+x2);
    cout << (x1+3);
    cout << (10+x1);
	
	Box x3;
    //cin >> x3;
    //cout <<x3;
	
}

#endif
/*******************************************************************************
* Chapter 7: Class and objects  PART -I
* Topics :
* KeyNotes:

	
********************************************************************************/
#if 0
class B
{
   public:
    void display(){
    	cout << "I am in B\n";
    }
};

class D:public B
{
	public:
    void display(){
    	cout << "I am in D\n";
    }
};

void test_overwritten()
{
	B b;
	D d;
	b.display();
	d.display();
	b.B::display();
}
#endif

#if 0
class B
{
   public:
   	B(){ cout<<"Cons of B called\n";   }
   	~B(){ cout<<"Dest of B called\n";	}
};

class D:public B
{
	public:
   	D(){ cout<<"Cons of D called\n";   }
   	~D(){ cout<<"Dest of D called\n";	}
};

void test_const_oder_call()
{
D d;
}
#endif

#if 0
class B
{
   public:
   void show(){}  //<<<<<<<<<<< request member for show is ambigious without virtusl clas
   		cout <<"Show on base\n";
   	}
};

class D1: virtual public B{ };
class D2: virtual public B{ };
class C: public D1, public D2
{
	public:
   	void display(){
   		cout <<"Show on base\n";
   	}
};
void test_vertual class()
{
C c;
c.display();
c.show();
}
#endif

#if 0 
NOT WORKING
class B1
{
   int i,j;
   public:
   B1(int i,int j){}
   i=i;j=j;
   }
   void show()
   {
   	cout <<i<<j<<endl;
   }
};

class B2
{
   int a,b;
   public:
   B2(int a,int b){}
   a=a;b=b;
   }
   void show(){
   	cout<<a<<b;
   }
};

class C: public B1, public B2
{
	int x,y;
	public:
	C(int i,int j,int a,int b, int x, int y) : B1(a,b), B2(i,j), x(x),y(y)
	{ }
   	void show(){
   		cout <<x<<y<<endl;
   		B1::show();
   		B2::show();
   	}
};
void test_initialization_list()
{
C c(1,2,3,4,5,6);
c.show();
}
#endif

#if 0
class X{
	int i;
	public:
		X(){
			i=0;
		}
		X(int i):i(i){
		}
		void show(){
			cout<<i<<endl;
		}
};

class Y
{
	X l[10];
	public:
		Y(){
			for (int i=0;i<10;i++)
			{
				l[i] = X(i);
			}
		}
		void show(){
			for (int i=0;i<10;i++)
			  l[i].show();
		}
};
void test_composition()
{
	Y y; y.show();
	
}
#endif

#if 0
NOT WORKING
class A
{
	int i;
	public:
		A(int i){
			this->i =i;
		}
		A max(A & a)
		{
			if (a.i >i)
			  return a;
			else
			  return *this;
		}
		A operator ++()
		{
			i++;
			return *this;
		}
		A operator ++( int i) //prefix
		{
			A temp = *this;
			i++;
			return temp;
		}
		void show()
		{
			cout <<"A: "<<i<<endl;
		}
};

void test()
{
	A a1(3);
	A a2(5);
	//(a1.max(a2)).show();
	A b = (a1 ++);
	b.show();
	a1.show();
}
#endif

#if 0
class A
{
	public:
		int a;
		void show(){
			cout<<"Show in A\n";
		}
		virtual void display()
		{
			cout<<"Display in A\n";
		}
};
class B:public A
{
	public:
		int b;
		void show(){
			cout<<"Show in B\n";
		}
		void display()
		{
			cout<<"Display in B\n";
		}
};

void test_runtimePoly_dynamic_binding()
{
	A a;
	B b;
	
	A *aptr;
	B *bptr;
	
	// base ptr to base obj
	aptr = &a;
	aptr->a=10;
	aptr->show();
	aptr->display();
	 
	// base ptr to derived obj
	aptr = &b;
	//aptr->b =10; CANOT ACCESS
	((B*)aptr)->b =10; // WILL WORK WITH TYPE CASE
	aptr->show(); // STILL SHOWS A's  as show is not virtual
	((B*)aptr)->show();	
	aptr->display(); // WILL DISPLAY B..without Type case ..MAJIC 
	
	
	//derived point to base 
	// bptr = &a; // Cannot assign directly need a cast
	bptr =(B*)&a; 
	bptr->a=10;
	bptr->show(); // B's Show
	bptr->display(); //A's display as virtual
	
	// derived pointer to derived object
	bptr =&b;
	bptr->b=1;
	bptr->show();
	bptr->display();
}

#endif
/*******************************************************************************
* Chapter 8: C++ I/O operations 
* Topics :
* KeyNotes:
8.1 Console Operation

8.2 File Input / Output
********************************************************************************/

/*******************************************************************************
* Chapter 9: Exception Handaling in C++ 
* Topics :
* KeyNotes:
********************************************************************************/

/*******************************************************************************
* Chapter 10: Templates and Generic Programming
* Topics :
* KeyNotes:

********************************************************************************/
#if 0
/* Ex: Template functions */
template <class T>
T mymax( T a, T b)
{	
	//cout<<"join:"<< (a + b);
	return (a>b?a:b);
}

/* Mixed Template */
template <class X, class Y>
void display(X a, Y b)
{ 
   cout << a <<" "<<b;
}
 
int main()
{
	cout << mymax(2,3)<<endl;
	cout << mymax("hello","wordl")<<endl;
	
	display(2,3.555);
}
#endif

#if 0
/* Ex : Template Classes */
template <class T, int size>
class stack
{
	T a[size];
	int top;
	public:
		stack(){
			top = -1;
			//size ++; <<< Here size is const..
		}
		void push(T i){
			if (top >size-2)
			  cout<<"Stack full\n";
			 else{
			 	   top ++;
			       a[top] = i;	
			     }
		}
		T peek(){
			if(top ==-1)
			  cout <<"No item\n";
			else
			  return a[top];
		}
		T pop(){
			if(top ==-1)
			  {
			  	cout <<"No item\n"; return NULL;
			  }
			else
			  return a[top--];
		}
		void display(){
			for (int i=top;i>=0;i--) cout<<a[i]<<endl;
		}
		
};

int main()
{
	stack<char *,3> s;
	s.display();
	s.push("Hell");s.push("Radha");s.push("Hari");s.push("Ram");
	s.display();
	cout << s.peek();
	cout <<s.pop();
	cout <<s.pop();
	cout<<s.pop();
	cout<< s.pop();
}
#endif

/*******************************************************************************
* Chapter 11. STL and Algorithms
* Topics :
* KeyNotes:

	    
********************************************************************************/
#if 0
/* Vector ::  STL http://www.cplusplus.com/reference/vector/vector/rbegin/ */
#include <vector>
#include<algorithm>
int main()
{
	vector<int> v;
	
	/*Task 1: Insert element in vector from Back*/
	v.push_back(1);	v.push_back(2);	v.push_back(3);	v.push_back(4);	v.push_back(5);	v.push_back(6);
	
	/* Size and Capcity */
	cout <<"Size:"<<v.size()<<" Capacity: "<< v.capacity()<<endl;
	
	/* Trask 2: Print the vector */
	cout <<"\nVector :\n"; for (int i=0;i<v.size();i++)  cout << v[i]<<endl;
	
	/* Tarsk 3: Delete an Elements from Back*/
	 v.pop_back();
	 v.pop_back();
	cout <<"\nVector :\n"; for (int i=0;i<v.size();i++)  cout << v[i]<<endl;
	
	/*Task 4: Print front and back one */
	cout << "Front: "<<v.front() <<" Back: "<<v.back()<<endl;
	
	/*Task 5: Interator to print the info*/
	vector<int>::iterator itr;
	for (itr = v.begin();itr!=v.end();itr++) {
		cout <<*itr<<" ";
	}
	cout <<endl;
	for (itr = v.end()-1;itr!=v.begin()-1;itr--){
		cout <<*itr<<" ";
	}
	
	/*Task 6: rbigin and rend and revrse Iterator*/
	cout<<endl;
	vector<int>::reverse_iterator rit;	
	for(rit = v.rbegin(); rit != v.rend();++rit );{
		cout<<(*rit)<<"  ";
	}	
    return 0;	
}
#endif

#if 0
/* DEQUE : http://www.cplusplus.com/reference/deque/deque/begin/ */
#include<deque>
int main()
{
	/* 1. Create a Deq */
	deque <int> q1 ; //empty
	deque<int> d(10,0); //10 with value 0
	cout <<"\nDeQueue: [ "; for (int i=0;i<d.size();i++)  cout << d[i]<<" "; cout <<"]\n";
	
	/* Insert from Both Side */
	d.push_back(10);
	d.push_front(10);
	cout <<"\nDeQueue: [ "; for (int i=0;i<d.size();i++)  cout << d[i]<<" "; cout <<"]\n";
	
	/* Delete from Both Side */
	d.pop_back();
	d.pop_front();
	cout <<"\nDeQueue: [ "; for (int i=0;i<d.size();i++)  cout << d[i]<<" "; cout <<"]\n";
	
}
#endif

#if 0
/* LIST : DOUBLE LINKED LIST: http://www.cplusplus.com/reference/list/list/insert/ */
#include<list>
int main()
{
	/* 1. Create a Deq */
	list<int> l(5,0); //5 with value 0
	
	/*Print :we dont have Random acess by index */
	list<int>::iterator it;
	cout <<"\nLIST: [ "; for (it=l.begin();it!= l.end() ;it++)  cout << *it <<" "; cout <<"]\n";
	
	/* Insert from Both Side */
	l.push_back(99);
	l.push_front(99);
	cout <<"\nLIST: [ "; for (it=l.begin();it!= l.end() ;it++)  cout << *it <<" "; cout <<"]\n";

	/* Delete from Both Side */
	l.pop_back();
	l.pop_front();
	cout <<"\nLIST: [ "; for (it=l.begin();it!= l.end() ;it++)  cout << *it <<" "; cout <<"]\n";

}
#endif

#if 0
//SET And MultiSet Operation.
#include<set>
int main()
{
	/* 1. Create a set  */
	set<int> s; //5 with value 0
	multiset<int> m; //5 with value 0
	
	
	/* insert into Set : Insert 2 times */
	for(int i=1;i<=5;i++){
		s.insert(i);
		s.insert(i);
		m.insert(i);
		m.insert(i);
	}
	
	/*Print :Printing the set */
	set<int>::iterator it;
	cout <<"\nLIST: [ "; for (it=s.begin();it!= s.end() ;it++)  cout << *it <<" "; cout <<"]\n";
	multiset<int>::iterator it1;
	cout <<"\nMultiSet: [ "; for (it1=m.begin();it1!= m.end() ;it1++)  cout << *it1 <<" "; cout <<"]\n";
		
	/* is memmber test */
	it = s.find(9);
	if(it !=s.end())
	  cout<<"found:"<<*it;
	else
	  cout <<"Not found";
	  
	/* Delete an item from a set : setObject.erase (key) or setObject.erase (it);or setObject.erase (iLowerBound, iUpperBound);  */
	s.erase(1);
	m.erase(1);
	cout <<"\nLIST: [ "; for (it=s.begin();it!= s.end() ;it++)  cout << *it <<" "; cout <<"]\n";
}
#endif

#if 0
#include<map>
#include<string>
int main()
{
	/* 1. Create a map and multi map  */
	map<int,string> m;
	multimap<int,string> mm;
	
	/*Insert into Map and multimap */
	m.insert(make_pair(1,"OneOne"));
	m.insert(make_pair(1,"One"));
	m.insert(make_pair(2,"TwoTwo"));
	m.insert(make_pair(2,"Two"));
	
	mm.insert(make_pair(1,"OneOne"));
	mm.insert(make_pair(1,"One"));
	mm.insert(make_pair(2,"TwoTwo"));
	mm.insert(make_pair(2,"Two"));
	
	/*Display the map and multimap */
	map<int,string>::iterator it;
	multimap<int,string>::iterator it1;
    cout <<"\nMap: \n"; for (it=m.begin();it!= m.end() ;it++)  cout << it->first <<" : "<<it->second<<endl; cout <<"]\n";
	cout <<"\nmultiMap: \n"; for (it1=mm.begin();it1!= mm.end() ;it1++)  cout << it1->first <<" : "<<it1->second<<endl; cout <<"]\n";
   
   /* Fins an Elemnt -- Just like as before*/
   it = m.find(1);
   if(it!= m.end())
     cout<<it->first<<" "<<it->second;
}
#endif

#if 0
#include<stack>
/* Stack operation */
int main()
{
	stack<int> s;
	/* Insert ,size,getTop, pop */
	s.push(10);s.push(20);s.push(30);
	cout<<s.size()<<endl;
	cout<<s.top()<<endl;
	cout<<s.empty()<<endl;
	s.pop();
	cout<<s.top()<<endl;
}
#endif

#if 0
/* QUEUE Operation */
#include<queue>
int main()
{
	queue<int> q;
	/* various operation */
	q.push(10);q.push(20);q.push(30);
	cout<<"Size"<<q.size()<<endl;
	cout<<"Front:"<<q.front()<<endl;
	cout<<"back: "<<q.back()<<endl;
	cout<<"IsEmpty: "<<q.empty()<<endl;
	q.pop();
	cout<<"Front:"<<q.front()<<endl;
	cout<<"back: "<<q.back()<<endl;
			
}
#endif

#if 0
/* Heap operation : This is a Max heap */
#include<queue>
int main()
{
	priority_queue <int> pq;
	cout<<"Inserting: 10,5,100,200"<<endl;
	pq.push(10);pq.push(5);pq.push(100);pq.push(1000);
	cout <<"Poping out :";
	while(!pq.empty()){
		cout<<pq.top()<<" ";
		pq.pop();
	}
}
#endif

#if 0
/* Use of Priority Que for Useful operation 
- We have huge list of studnet
- Find out max 10 student having least marks.
*/
#include <string>
#include<queue>
class student
{
	string name;
	int marks;
	public:
		student(string name,int marks):name(name),marks(marks){
		}
		void show(){
			cout<<"Name: "<<name<<" Marks: "<<marks<<endl;
		}
		//define a < comrasism here 
		friend bool operator< (const student &s1, const student &s2); 
};
bool operator< (const student &s1, const student &s2)
{
	return s1.marks > s2.marks;
}

int main()
{
	priority_queue<student> pq;
	
	student s1("Dipankar",50);
	student s2("Ram",70);
	student s3("hari",10);
	pq.push(s1);
	pq.push(s2);
	pq.push(s3);
	
	while(!pq.empty()){
		student s = pq.top();
		s.show();
		pq.pop();
	}
}

#endif

/*Some String related Stuff */
#include<string>
int main()
{
	/* 1. Create String */
	string s1;cout<<s1;
	string s2("Dipankar");
	string s3 ="hello";
	s1= s3 +" "+ s2; cout <<s1<<endl;
	
	/* 2. Input and output */
	//cin >> s1; cout <<s1; <<<<<< Space Termited
	 //getline(cin,s1);cout<<s1;
	 
	 /* 3. String Menupulation */
	 s1= "hello"; s2=s1; cout<<"IsSameFile: "<<(s1==s2)<<endl;
	 s1= "abc"; s2="def"; cout<<"CMP: "<<(s1 < s2)<<endl;
	 s1= "abc"; s2="def"; cout<<"CMP: "<<(s1  > s2)<<endl;
	 s1= "abc"; s2="def"; cout<<"CMP: "<<(s1 !=s2)<<endl;
	 
	 s1= "helloDipankar";
	 cout<<"Size: "<<s1.size()<<" "<<s1.length()<<" "<<s1.capacity()<<" "<<s1.max_size()<<"  "<<s1.empty()<<endl;	 
	 
	 string s="HelloDipankar";
	 for(int i=0;i<s.length();i++) cout<<s[i]<<s.at(i);
	 
	 cout<<endl<<s.find("a")<<" "<<s.find_first_of('a')<<" "<<s.find_last_of('a')<<endl;
	 //cout<<endl<<s.find("DD")<<" "<<s.find_first_of('E')<<" "<<s.find_last_of('E');
	 
	 s1="Hello";
	 s2="Diapnakr";
	 cout<< (s1+s2)<<" | "<<s1.append(s2)<<endl;
	 
}




/*******************************************************************************
* Chapter 12: C++ Advance Topics I : Multithreading
* Topics :
* KeyNotes:
********************************************************************************/

/*******************************************************************************
*  Chapter 12: C++ Advance Topics II : Signal Handaling
* Topics :
* KeyNotes:
********************************************************************************/

/*******************************************************************************
*  Chapter 12: C++ Advance Topics III : Name Spaces
* Topics :
* KeyNotes:
********************************************************************************/

/*******************************************************************************
*  Chapter 12: C++ Advance Topics IV : Multithreading
* Topics :
* KeyNotes:
12.1 Basic Concept 
	- Multithreading is a specialized form of multitasking
	- multitasking is the feature that allows your computer to run two or more programs concurrently. 
	- Process-based multitasking handles the concurrent execution of programs.
	- Thread-based multitasking deals with the concurrent execution of pieces of the same program.
	- A multithreaded program contains two or more parts that can run concurrently
	- We are using Linux OS ,multi-threaded C++ program using POSIX or pthread
12.2 Pthread Library use
	- #include <pthread.h>
	- Cretaing a thread
		* pthread_create (ref to Ptrread_object, attributes, start_routine_or_code_to execute, arg_list)
		* int pthread_create(pthread_t*, const pthread_attr_t*, void* (*)(void*), void*)
	- Terminating a thread
		* pthread_exit (status) => Terminate a Thread
	- Block the calling thread iuntil spacofied thread terminate
		* pthread_join (threadid, status) =>int pthread_join(pthread_t, void**)
	-  Detach a treaded and Let's them work indipendently , never wait for join
		* pthread_detach (threadid) 
12.3 Issue and Resolution of thread operation.	
    12.3.1 Thread syncronization with Lockinga nd Unlocking
    - Create a Lock
    	pthread_mutex_t lock_x;
    	int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *mutexattr);
    - Locking and unlocking 
    	int pthread_mutex_lock(pthread_mutex_t *mutex);
		int pthread_mutex_trylock(pthread_mutex_t *mutex);
		int pthread_mutex_unlock(pthread_mutex_t *mutex);
	12.3.2 Thread Syncronization usig wait and Signal Opeartion
		- Sipport Conditinal Locking mechnisam
		int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
		int pthread_cond_signal(pthread_cond_t *cond);
		int pthread_cond_broadcast(pthread_cond_t *cond);
		- pthread_cond_wait() puts the current thread to sleep. It requires a mutex of the associated shared resource value it is waiting on.
		- pthread_cond_signal() signals one thread out of the possibly many sleeping threads to wakeup.
		- pthread_cond_broadcast() signals all threads waiting on the cond condition variable to wakeup. 
		
		- Create conditial lock : pthread_cond_t sig_consumer
		- Sleep a thread for an event : pthread_cond_wait(&sig_consumer, &lock);
		- Wake up thread : pthread_cond_signal(&sig_consumer);
	12.3.3  Inter thread/Process comminication
		- Number of way to do that
		a. Using shareed memory
		b. Using message passing ( Called Message Queue)
	  
	
********************************************************************************/
#if 0
/*Simple Thread test*/
#include<iostream>
#include<pthread.h>
using namespace std;

#define MAX_THREAD 5
void * print(void * tid)
{
  for (int i=0;i<5;i++)
    cout <<"Thread #"<<(long)tid <<": Hello "<<i<<endl;
  pthread_exit(NULL);
}

int main()
{
  pthread_t t[5];
  int ret;
  for (int i=0;i<5;i++)
  {
    cout<<"Main: Cretaing thread: "<<i<<endl;
    ret = pthread_create(&t[i],NULL,print,(void*)i);
    if(ret)
    {
      cout << "Not able to create thread"<<ret<<endl;
    }
  }
pthread_exit(NULL);

}

//g++ thread1.cpp -lpthread && ./a.out  
#endif


#if 0
/* Message passing example with thread join */
#include<iostream>
#include<pthread.h>
using namespace std;

struct MSG{
        int tid;
        char *info;
};
#include<iostream>
#include<pthread.h>
using namespace std;

struct MSG{
        int tid;
        char *info;
};

void * print(void * m)
{
void * print(void * m)
{ 
  MSG *msg = ( MSG* ) m;
  cout<<"Recined MesageLike ID:"<<msg->tid<<" info: "<<msg->info<<endl;
  pthread_exit(NULL);
}
int main()
}
int main()
{
  pthread_t t[5];
  int ret;
  cout <<"Main(): Start.."<<endl;
  for (int i=0;i<5;i++)
  {
    /* Creating message */
    MSG msg;
    msg.tid = i;
    msg.info ="hello Dipankar";

    /* Creating Thread */
    ret = pthread_create(&t[i],NULL,print,(void*)&msg);
    if(ret)
    {
      cout << "Not able to create thread"<<ret<<endl;
    }
  }
  /*  Wait for all thread to join first */
  for (int i=0;i<5;i++)
  {
    ret = pthread_join(t[i],NULL);
    if(ret)
    {
      cout <<"Error is Thread Join"<<endl;
    }
  }
  cout <<"Main() : Exit "<<endl;
  pthread_exit(NULL);

}

//g++ thread1.cpp -lpthread && ./a.out  
                                        
#endif

#if 0
/* Locking and Unlocking */
#include<iostream>
#include<pthread.h>
using namespace std;

struct MSG{
        int tid;
        char *info;
};
#include<iostream>
#include<pthread.h>
using namespace std;

struct MSG{
        int tid;
        char *info;
};

void * print(void * m)
{
void * print(void * m)
{ 
  MSG *msg = ( MSG* ) m;
  cout<<"Recined MesageLike ID:"<<msg->tid<<" info: "<<msg->info<<endl;
  pthread_exit(NULL);
}
int main()
}
int main()
{
  pthread_t t[5];
  int ret;
#include<iostream>
#include<pthread.h>
using namespace std;

/* This is a Message Structure */
struct MSG{
        int tid;
        char *info;
        float money;
};

/* Global Shared data and thread lock */
float total_money;
pthread_mutex_t lock;

/* Thread handaling Code */
void * print(void * m)
{
  MSG *msg = ( MSG* ) m;
  cout<<"Recined MesageLike ID:"<<msg->tid<<" info: "<<msg->info<<endl;

/* Global Shared data and thread lock */
float total_money;
pthread_mutex_t lock;

/* Thread handaling Code */
void * print(void * m)
{
  MSG *msg = ( MSG* ) m;
  /* Now the share and print will be inside lock and unlock */
  pthread_mutex_lock(&lock);
  cout<<"Recined MesageLike ID:"<<msg->tid<<" info: "<<msg->info<<endl;
  total_money += msg->money;
  cout <<" Now Total Price :" <<total_money<<endl;
  pthread_mutex_unlock(&lock);
  sleep(1);
  pthread_exit(NULL);
}

/* Start Main Program */
int main()
{
  pthread_t t[5];
  int ret;

  /* Build 5 message */
  MSG m[5];
  for (int i=0;i<5;i++)
  {
    m[i].tid =(i+1);
    m[i].info ="Hello Dipankar";
    m[i].money = 10.0 *(i+1);
  }

  /* Inililize shared data and lock */
  total_money =0.0;
  pthread_mutex_init(&lock,NULL);

  cout <<"Main(): Start.."<<endl;
  for (int i=0;i<5;i++)
  {
    /* Creating Thread */
    ret = pthread_create(&t[i],NULL,print,(void*)&m[i]);
    if(ret)
    {
      cout << "Not able to create thread"<<ret<<endl;
    }
  }
  /*  Wait for all thread to join first */
  for (int i=0;i<5;i++)
  {
    ret = pthread_join(t[i],NULL);
    if(ret)
    {
      cout <<"Error is Thread Join"<<endl;
    }
  }
  cout <<"Main() : Exit "<<endl;
  pthread_exit(NULL);

}

//g++ thread1.cpp -lpthread && ./a.out  
#endif

#if 0
/* Wait and Single Version for Producer and Consumer */
#include<iostream>
#include<pthread.h>
using namespace std;

/* This is a Share Buffer 
 We should use Lock to access these shareed varaible*/
#define B_SIZE 10
#define COMSUME_TIME 1
#define PROD_TIME 10
int buff[B_SIZE+1];
int cur_index = -1;
          
         
/* Global thread lock and Conditinal Lock*/
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t sig_consumer= PTHREAD_COND_INITIALIZER;
pthread_cond_t sig_producer= PTHREAD_COND_INITIALIZER;
             
      
/* Produces thread handaling Code */
void * producer(void * dummy)
{   
  cout <<"Prod: Started.."<<endl;
  int item= 0;
  while(1)
  {    
    
    /* if no space in buff , Produce Wait */
    pthread_mutex_lock(&lock);
    if(cur_index == B_SIZE)  
        pthread_cond_wait(&sig_producer, &lock);
    pthread_mutex_unlock(&lock);
    /* Produce An Item and place it to buffer */
     item ++;
     sleep(PROD_TIME);
     cout <<"prod: Generate "<<item<<endl;

     /* Place the item in the buff */
     pthread_mutex_lock(&lock);
     cur_index++;
     buff[cur_index]=item;
     pthread_mutex_unlock(&lock);
     /* Now Signal comsuper ..*/
     pthread_cond_signal(&sig_consumer);

  }
}

/* Consumer thread */
void * consumer(void * dummy)
{
  cout <<"Con: Started.."<<endl;
  while(1)
  {

     /* If No item Single Producer to Prouce Item and wait.. */
     pthread_mutex_lock(&lock);
     if(cur_index < 0)
       {
          pthread_cond_signal(&sig_producer);
          pthread_cond_wait(&sig_consumer, &lock);
       }
     pthread_mutex_unlock(&lock);

     /* Now get the Item from buffer */
     pthread_mutex_lock(&lock);
     int item = buff[cur_index];cur_index--;
    /* Single Comsumer if it create some space */
     pthread_cond_signal(&sig_producer);
     pthread_mutex_unlock(&lock);

     /* Consume the item */
     sleep(COMSUME_TIME);
     cout <<"con: Consume "<<item<<endl;

  }
}

/* Start Main Program */
int main()
{
  pthread_t t[2];
  int ret;

  /* Inililize shared data and lock */
  pthread_mutex_init(&lock,NULL);

  /* Create consumer & producer threads. */
  if ((ret= pthread_create(&t[0], NULL, consumer, NULL)))
    cout<< "Error creating the consumer thread..\n"<<endl;

  if ((ret= pthread_create(&t[1], NULL, producer, NULL)))
    cout << "Error creating the producer thread..\n"<<endl;

  /* Wait for consumer/producer to exit. */
  for (int i= 0; i < 2; i ++)
    pthread_join(t[i], NULL);

  cout <<"Main() : Exit "<<endl;
  pthread_exit(NULL);

}

//g++ thread2.cpp -lpthread && ./a.out

#endif

#if 0
/* IPC using message Queue */
/* Message Sender */
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

#define MAXSIZE     128

struct MSG
{
    long    mtype;
    char    mtext[MAXSIZE];
};

int main()
{
    int msqid;
    int msgflg = IPC_CREAT | 0666;
    int count = 0;
    /* Getting message Queue */
    key_t  key = 1234;
    if ((msqid = msgget(key, msgflg )) < 0)   //Get the message queue ID for the given key
    {
      cout <<"Eroor while getting Quie ID"<<endl;
    }
    while(1){
      cout << "Genaring messages "<<count<<endl;count ++;
      /* Building Message */
      MSG  sbuf;
      sbuf.mtype = 1;
      strcpy(sbuf.mtext,"Hello World");
      /* Sending messages */
      size_t buflen = strlen(sbuf.mtext) + 1 ;
      if (msgsnd(msqid, &sbuf, buflen, IPC_NOWAIT) < 0){
        cout <<" Not able to send msg \n";
      }
    else
      cout << "Message Sent\n";
    sleep(2);
  }
}

// SEE the message by ipcs -q
//g++ mq_sender.cpp -lpthread && ./a.out


/* Message Receiver */
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

#define MAXSIZE     128

struct MSG
{
    long    mtype;
    char    mtext[MAXSIZE];
};

int main()
{
    int msqid;
    int msgflg = IPC_CREAT | 0666;
    int count = 0;
    /* Getting message Queue */
    key_t  key = 1234;
    if ((msqid = msgget(key, msgflg )) < 0)   //Get the message queue ID for the given key
    {
      cout <<"Eroor while getting Quie ID"<<endl;
    }
    while(1){
      cout << "Getting messages "<<count<<endl;count ++;
      /* getting Message */
      MSG  rcvbuffer;
      if (msgrcv(msqid, &rcvbuffer, MAXSIZE, 1, 0) < 0)
      { cout <<"ERROR"<<endl;
      }
      else
      {
        cout <<"Message is "<< rcvbuffer.mtext<<endl;
      }
    sleep(1);
  }
}

// SEE the message by ipcs -q
//  RUn : g++ mq_recv.cpp -lpthread && ./a.out

#endif

/*******************************************************************************
* Chapter 12: C++ Advance Topics V : Socket Programming
* Topics :
* KeyNotes: http://www.binarytides.com/socket-programming-c-linux-tutorial/
********************************************************************************/

/*******************************************************************************
* Chapter 12: C++ Advance Topics VI : CGI Programming
* Topics :
* KeyNotes:
********************************************************************************/

/*******************************************************************************
* Chapter 12: C++ Advance Topics VII : Smart Pointers
* Topics :
* KeyNotes:
********************************************************************************/


