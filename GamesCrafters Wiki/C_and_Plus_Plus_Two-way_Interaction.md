C\_and\_Plus\_Plus\_Two-way\_Interaction
========================================

*Written by Haley Nguyen* Here, I demonstrate that a method in a C++ class can call a method in a C code file. Then, the callee function, in turn, calls another function in the C++ class. I also demonstrate that the C++ function can also share a variable with the C code.

main.cpp
--------

`#include `<iostream>
`#include "code.h"`
`using namespace std;`
`void Foo::foo() {`
`   cout << "foo()\n";`
`   bar();`
`}`
`void Foo::a() {`
`   cout << "a()\n"; `
`}`
`int main (void) {`
`   Foo* f = new Foo();`
`   foo = f;`
`   f->foo();`
`   cout << "x = " << f->x << endl;`
`   return 0;`
`}`
