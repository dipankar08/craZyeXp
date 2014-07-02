#include<iostream>
using namespace std;
namespace aaa{
  void display() {cout<<"Inside AAA\n";}
}
namespace bbb{
  void display() { cout <<" Inside BBB\n";}
}

namespace ccc{
  void display(){ cout<<"inside CCC\n";}
  namespace ddd{
    void display(){ { cout<<"inside CCC::DDD\n";}}
  }
}
using namespace ccc::ddd;
//using namespace bbb;>> error: call of overloaded splay() ambiguous
int main()
{
  aaa::display();
  bbb::display();
  display();
}
