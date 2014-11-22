/********************************************
* builder1.cpp:  Builder patteren
* Author :Dipankar Dutta.
* Description /Steps.
* Step1: We have Product, which need to build, define in a class...This contains a list o part need to be build this.
* step 2: We have a Ibuilder interface, which implement two builder Builder1 and Builder2, Bascially thease are two machines who
*        builder all  part of product using different materials.
* Step 3: We have a Director ( bacially a person, who knows step by step of running Buildre(or machine ) to get the product out .
*
* Sumary : Step-By-Step Contracting an Object with some Algorithms
*********************************************/
#include <iostream>
#include <vector>

using namespace std;

class Product{
    private:
        vector<string> _parts;
public:
    void add(string part){
        _parts.push_back(part);
    }
    void show(){
        cout<<endl<<"All parts are:\n";
        for(int i=0;i<_parts.size();i++){
            cout<<_parts[i].c_str()<<endl;
        }
    }
};

class IBuilder{
protected:
    Product p;
public:
    virtual void buildPartA() =0;
    virtual void buildPartB() =0;
    virtual void buildPartC() =0;
    virtual Product getResult() =0;
};
class Builder1:public IBuilder{
public:
    void buildPartA(){ p.add(string("PartA from Bilder 1"));  }
    void buildPartB(){ p.add(string("PartB from Bilder 1"));  }
    void buildPartC(){ p.add(string("PartC from Bilder 1"));  }
    Product getResult(){return p;}
};
class Builder2:public IBuilder{
public:
    void buildPartA(){ p.add(string("PartA from Bilder 2"));  }
    void buildPartB(){ p.add(string("PartB from Bilder 2"));  }
    void buildPartC(){ p.add(string("PartC from Bilder 2"));  }
    Product getResult(){return p;}
};

class Director{
private:
    IBuilder *builder;
public:
    void setBuilder(IBuilder *b){
        builder=b;
    }
    void constract(){  // Basically run the step or algorithms.
        builder->buildPartA();
        builder->buildPartC();
        builder->buildPartB();
        builder->getResult();
    }
};

int main() {
    cout << "Hello, World!" << endl;
    //Get The machine.. Choose one Builder..
    IBuilder * iBuilder = new Builder2();
    //Get the cook.. that is Director..
    Director director;
    // Cook Set the Builder/ which builder to use to amke the product...
    director.setBuilder(iBuilder);
    // Cook run the Algorithms
    director.constract();
    // getting the product from machine and shoing it..
    iBuilder->getResult().show();
    return 0;
}