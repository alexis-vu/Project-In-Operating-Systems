#include "LinkedList.h"

template <typename T>
ostream& operator<<(ostream& out, const LinkedList<T>& list) {
  if (list.head == nullptr) {
    out << "List is empty." << endl;
  }
  else {
    Node<T>* temp = list.head;

    while (temp != nullptr) {
      out << temp->getData() << " ";
      temp = temp->getNext();
    }
  }

  return out;
}

template <typename T>
LinkedList<T>::LinkedList() {
  head = nullptr;
  count = 0;
}

template <typename T>
LinkedList<T>::insert(const T& node) {
  Node<T>* newNode = new Node<T>(node, nullptr);

  if (head == nullptr) {
    head = newNode;
  }
  else {
    Node<T>* temp = head;
    while (temp->getNext() != nullptr) {
      temp = temp->getNext();
    }
    temp->setNext(node);
  }

  ++count;
}

template <typename T>
LinkedList<T>::count() const {
  return count;
}

template <typename T>
LinkedList<T>::destroyList() {
  Node<T>* temp = head;

  while (temp != nullptr) {
    head = head->getNext();
    delete temp;
    temp = head;
  }

  count = 0
}

template <typename T>
LinkedList<T>::~LinkedList() {
  destroyList();
}
