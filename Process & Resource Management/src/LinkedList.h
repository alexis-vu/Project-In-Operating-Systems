#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>
#include <string>
using namespace std;

template <typename T>
class Node {
private:
  T data;
  Node<T>* next;

public:
  Node(): data(NULL), next(nullptr) {}
  Node(const T& d, Node<T> *n) : data(d), next(n) {}
  Node<T>* getNext() const { return next; }
  T getData() const { return data; }
  void setData(const T& d) { data = d; }
  void setNext(Node<T>* n) { next = n; }
  ~Node(){}
};

template <typename T>
class LinkedList {

template<typename T>
friend ostream& operator<<(ostream& out, const LinkedList<T>& list);

private:
    Node<T>* head;
    int count;

public:
  LinkedList();
  void insert(const T& node);
  int getCount() const;
  void destroyList();
  ~LinkedList();
};

#endif
