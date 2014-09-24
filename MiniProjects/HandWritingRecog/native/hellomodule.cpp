#include <iostream> // std::cout
#include <utility>  // std::make_pair
#include <boost/foreach.hpp>
#include <boost/python.hpp>
#include <boost/python/stl_iterator.hpp>

using namespace std;
using namespace boost::python::list
 
void  say_hello(int a, const list& pylist) {
 cout << "Hello " << "!\n";
 typedef boost::python::stl_input_iterator<int> iterator_type;
  BOOST_FOREACH(const iterator_type::value_type& data, 
                std::make_pair(iterator_type(list), // begin
                               iterator_type()))    // end
  {
    std::cout << data << std::endl;
  }
}
 
 
 
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
using namespace boost::python;
 
BOOST_PYTHON_MODULE(hello)
{
    def("say_hello", say_hello);
}
