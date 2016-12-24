#include <iostream>
#include <vector>

using namespace std;


class Element {

};


int main() {
  Element element;
  std::vector<Element> elements;

  cout << "hello" << endl;

  elements.push_back(element);

  cout << "address of elements[0] is " << &elements[0] << endl;
}
