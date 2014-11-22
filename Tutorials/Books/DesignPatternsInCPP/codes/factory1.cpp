/***********************************************
*  Factory1.cpp: Factory Pattern in C++
*  Step1: We have IProduct Abstract class - having two concrete class Product1 and Product2
*  Step2: We have IFactory Abstract class and Factory which crete and return Product based on a type flag
*  Step3. In Main program, we are getting different product from factory by spacifing the tyep..
*
*  That;s It..
*
*  Summary : Generate Object Based on the type flag.
*/

#include <iostream>
using namespace std;

/* Interface Iproduct and It's Two Implementations. */
class IProduct{
public:
    virtual void showProduct() =0;
};

class Product1: public IProduct{
public:
    void showProduct(){
        cout<<"I am product 1"<<endl;
    }
};
class Product2: public IProduct{
public:
    void showProduct(){
        cout<<"I am product 2"<<endl;
    }
};

/* factory and It's Implemenation */
class IFactory{
public:
    virtual IProduct * getProduct(int type) = 0;
};

class Factory: public IFactory{
public:
    /* This method Crete objcet based on the type flag....*/
    IProduct * getProduct(int type){
        switch(type){
            case 1: return new Product1();
            case 2: return new Product2();
            default: cout <<"No product found" <<endl;
        }
    }
};


int main() {
    cout << "Hello, actory 1" << endl;
    Factory f = Factory();
    /* See we have use common interface IProduct and Dont have any Idea of which product Class Object is return
    Decision made based on type...
    That's the majic of hiding Implementations, DO ANYTHING JUST SEEING THE INTERFACE>>
     */
    IProduct *p1 = f.getProduct(1);p1->showProduct();
    IProduct *p2 = f.getProduct(2);p2->showProduct();
    return 0;
}
