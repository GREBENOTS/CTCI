using System;
using System.Collections.Generic;

namespace csharp.Chapter2 {
    public class LinkedList {
        Node head = null;

        public LinkedList() {
            this.head = null;
        }

        public void RemoveDupes() {
            if(this.head == null) { return; }

            HashSet<int> seen = new HashSet<int>();
            Node n = this.head;
            int count = 0;
            while(n != null) {
                if(seen.Contains(n.data)) {
                    n = n.next;
                    this.RemoveAtIndex(count);
                    continue;
                } else {
                    seen.Add(n.data);
                }
                n = n.next;
                count++;
            }
        }

        public void InsertAtBeginning(int data) {
            Node node = new Node(null, data);
            this.head = node;
        }

        public void InsertAtEnd(int data) {
            if(this.head == null) {
                this.head = new Node(null, data);
                return;
            }

            Node n = this.head;
            while(n.next != null) {
                n = n.next;
            }
            n.next = new Node(null, data);
        }

        public void InsertAtIndex(int index, int data) {
            if(index < 0 || index >= this.Length()) {
                throw new IndexOutOfRangeException("The index is not valid");
            }

            if(index == 0) {
                this.InsertAtBeginning(data);
                return;
            }

            int count = 0;
            Node n = this.head;
            while(n != null) {
                if(count == index - 1) {
                    Node node = new Node(n.next, data);
                    n.next = node;
                    break;
                }

                n = n.next;
                count++;
            }
        }

        public void RemoveAtIndex(int index) {
            if(index < 0 || index >= this.Length()) {
                throw new IndexOutOfRangeException("The index is not valid");
            }

            if(index == 0) {
                this.head = this.head.next;
                return;
            }

            int count = 0;
            Node n = this.head;
            while(n != null) {
                if(count == index - 1) {
                    n.next = n.next.next;
                    break;
                }
                count++;
                n = n.next;
            }
        }

        public int Length() {
            int count = 0;

            Node n = this.head;
            while(n != null) {
                count++;
                n = n.next;
            }
            return count;
        }

        public void Print() {
            if(this.head == null) { Console.WriteLine("This LL is empty"); }

            Console.WriteLine();
            Node n = this.head;
            while(n != null) {
                Console.Write(n.data);
                Console.Write("--->");
                n = n.next;
            }
        }
    }
}
