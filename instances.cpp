#include <iostream>
#include <vector>

using namespace std;


class Element {

};


void link_nodes(std::vector<Element> *elements) {
    Element element;

    elements->push_back(element);

    cout << "address of elements[0] is " << &elements[0] << endl;
}

int main() {
  std::vector<Element> elements;

  cout << "hello" << endl;

  link_nodes(&elements);

  cout << "address of elements[0] is " << &elements[0] << endl;
}
