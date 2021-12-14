using System;
using csharp.Chapter2;

namespace csharp.Chapter2 {
    /// Remove Dups:  Write code to remove duplicated from an unsorted linked list.
    
    public class TwoOne {
        private Node head = null;

        public TwoOne() {
            Console.WriteLine("Question 2.1");
        }

        public void CreateTestData() {
            // 0, 2, 4, 6, 6, 2, 8, 0, 0, 6, 4, 2
            // Correct output should be:  0, 2, 4, 6, 8
            Node n = new Node(0);
            n.AppendToTail(2);
            n.AppendToTail(4);
            n.AppendToTail(6);
            n.AppendToTail(6);
            n.AppendToTail(2);
            n.AppendToTail(8);
            n.AppendToTail(0);
            n.AppendToTail(0);
            n.AppendToTail(6);
            n.AppendToTail(4);
            n.AppendToTail(2);
            this.head = n;
        }

        public void PrintNodes() {
            Node node = this.head;
            while (node != null) {
                Console.Write(node.data);
                Console.Write("--->");
                node = node.next;
            }
        }

        public void RemoveDupes(int data) {

        }
    }
}
