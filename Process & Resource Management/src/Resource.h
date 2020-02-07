#ifndef RESOURCE_H
#define RESOURCE_H

#include <iostream>
#include <string>
#include "LinkedList.h"
#include "Process.h"
using namespace std;

class Resource {
private:
  int state;
  LinkedList<int>* waitlist;

public:
  Resource();
};

#endif
