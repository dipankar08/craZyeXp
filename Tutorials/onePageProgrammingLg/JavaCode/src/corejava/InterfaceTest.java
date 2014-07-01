package corejava;

import java.util.Random;

interface Animals{
	void walk();
	void eat();
	void dance();
}
class DOG implements Animals{
	public void walk() {System.out.println("Dog : Walk");}
	public void eat(){System.out.println("Dog : eat");}
	public void dance(){System.out.println("Dog : eat");}
}
abstract class CAT implements Animals{
	public void walk() {System.out.println("CAT : Walk");}
	public void eat(){System.out.println("CAT : eat");}
	//public void dance(){System.out.println("CAT : eat");} << This is not implementd hence abstract
}

interface SharedConstants {
	int NO = 0;
	int YES = 1;
	int MAYBE = 2;
	int LATER = 3;
	int SOON = 4;
	int NEVER = 5;
}

class Question implements SharedConstants {
	Random rand = new Random();
	int ask() {
		int prob = (int) (100 * rand.nextDouble());
		if (prob < 30)
			return NO; // 30%
		else if (prob < 60)
			return YES; // 30%
		else if (prob < 75)
			return LATER; // 15%
		else if (prob < 98)
			return SOON; // 13%
		else
			return NEVER; // 2%
	}
}

class AskMe implements SharedConstants {
	static void answer(int result) {
		switch(result) {
		case NO:
			System.out.println("No");
			break;
		case YES:
			System.out.println("Yes");
			break;
		case MAYBE:
			System.out.println("Maybe");
			break;
		case LATER:
			System.out.println("Later");
			break;
		case SOON:
			System.out.println("Soon");
			break;
		case NEVER:
			System.out.println("Never");
			break;
		}
	}
}

public class InterfaceTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Animals a;
		a= new DOG();
		a.dance();
		a.eat();
		a.walk();
		
		//Animals a=new Animals()
		//CAT c = new CAT();
		
		Question q = new Question();
		AskMe.answer(q.ask());
		AskMe.answer(q.ask());
		AskMe.answer(q.ask());
		AskMe.answer(q.ask());
	}
}

