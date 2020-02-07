#include "LinkedList.h"
#include "Process.h"
#include "Resource.h"

#include <iostream>
#include <string>
using namespace std;

#define ERROR "error"
#define MAX_PROCESSES 100
#define MAX_RESOURCES 100

Process init();
void timeout();
void scheduler();

int main(int argc, char* argv[]) {
  Process pcb[MAX_PROCESSES];
  LinkedList<int> rl[MAX_PROCESSES];

  // bool done = false;

  pcb[0] = init();
  pcb[0].create(1, *rl);

  return 0;

  // while (!done) {
  //
  // }

  // TODO: create presentation shell
}

Process init() {
  Process* p = new Process();
  return *p;
}

void timeout() {

}

void scheduler() {

}
