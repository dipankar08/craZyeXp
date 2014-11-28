// code works because C++ allows you to overload operator(), the "function call" operator. The function call operator can take any number of arguments of any types and return anything it wishes to. (It's probably the most flexible operator that can be overloaded; all the other operators have a fixed number of arguments.) For ease of discussion, when an object's operator() is invoked, I'll refer to it as "calling" the object as though it were a function being called. 
// While overloading operator() is nice, the really cool thing about functors is that their lifecycle is more flexible than that of a function--you can use a a functor's constructor to embed information that is later used inside the implementation of operator(). 

#include <iostream>
 
class myFunctorClass
{
    public:
        myFunctorClass (int x) : _x( x ) {}
        int operator() (int y) { return _x + y; }
    private:
        int _x;
};
 
int main()
{
    myFunctorClass addFive( 5 );
    std::cout << addFive( 6 );
 
    return 0;
}
