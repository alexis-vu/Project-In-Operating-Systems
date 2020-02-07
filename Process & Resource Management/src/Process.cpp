#include "Process.h"

Process::Process() {
  id = 0;
  state = 1;
  parent = NULL;
  children = new LinkedList<Process>();
  resources = new LinkedList<Reosurce>();
}

Process::Process(int i, bool s, int p) {
  id = i;
  state = s;
  parent = p;
  children = new LinkedList<int>();
  resources = new LinkedList<int>();
}

void Process::create(int id, LinkedList<int>& rl) {
  Process* p = new Process(id, 1, this.id);
  p.id = id;
  p.state = 1;
  this.children.insert(&p);
  rl.insert(&p);
  cout << "Process " << p.id << " created" << endl;
}

void Process::destroy(Process& child) {
  child.children.destroyList();
  
}
