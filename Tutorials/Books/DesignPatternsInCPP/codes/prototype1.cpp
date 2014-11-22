/********************************************
* Singleton1.cpp: ProtoType pattern in C++
* Author :Dipankar Dutta.
* Description /Steps.
* Unfortunately, C++ doesn't have built-in support for dynamic instantiation, but the prototype pattern provides a standard way to add this feature to C++ programs:
*
* Step1: We have a prototype called IProduct, tghis is basically a prototype of product.
* Step 2: In IProduct act as a prototype, enable to add a new product type or clone from a extring prototype
* Step 3. We have tro Product; Prodcut1 and Product2, which extends Iproduuct.
* Step 4. The poweer feature is that, we can crete object of product 1 clone from another object of product 1/product two runtime..
* Step 5. All Property or datamember get copied.
*
* Summary: useful : Object Cloning..
*********************************************/
#include <iostream>
#include <map>
using namespace std;


#define IMPLEMENT_CLONE(TYPE) \
IProduct* clone() const { return new TYPE(*this); }

class IProduct
{
public:
    virtual ~IProduct() {}
    virtual IProduct* clone() const = 0;
    virtual void print() = 0;

    static IProduct* makeProduct(string type);
    static IProduct* addPrototype(string type, IProduct* p);
    static map<string, IProduct*> protoTable;
};

map<string, IProduct*> IProduct::protoTable;
IProduct* IProduct::makeProduct(string type)
{
    IProduct* proto;

    auto search = protoTable.find(type);
    if(search != protoTable.end()) {
        proto = search->second ;
        return proto->clone();
    }
    else {
           cout << "prototype not found Creteing one.";
    }
}
IProduct* IProduct::addPrototype(string type, IProduct* p)
{
    cout << "adding prototype for " << type << endl;
    protoTable[type] = p;
    cout << "done\n";
    return p; // handy

}


class Product1: public IProduct
{
private:
    string desc;
public:
    Product1(string desc){this->desc=desc;}
    IMPLEMENT_CLONE(Product1);
    void print(){cout <<" Product1:"<<desc<<endl;}

};

class Product2: public IProduct
{
private:
    string desc;
public:
    Product2(string desc){this->desc=desc;}
    IMPLEMENT_CLONE(Product2);
    void print(){cout <<" Product2:"<<desc<<endl;}

};


int main() {
    cout << "Hello, World!" << endl;
    string s = "bag";
    IProduct* bag= IProduct::addPrototype(s, new Product1("bag"));
    bag->print();
    IProduct *clone_bag = bag->clone();
    clone_bag->print();
    cout<< bag<<"##"<<clone_bag<<"is same"<<bool(bag == clone_bag); // they are not smae object,..
    return 0;
}