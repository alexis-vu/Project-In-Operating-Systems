#ifndef PROCESS_H
#define PROCESS_H

#include <iostream>
#include <string>
#include "LinkedList.h"
#include "Resource.h"
using namespace std;

class Process {
private:
  int id;
  bool state;
  int parent;
  LinkedList<int>* children;
  LinkedList<int>* resources;

public:
  Process();
  Process(int id, bool s, int p);
  void create(int id, LinkedList<int>& readyList);
  void destroy(Process& child);
  void request(Resource& r);
  void release(Resource& r);
};

#endif
