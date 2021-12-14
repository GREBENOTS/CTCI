using System;
namespace csharp.Chapter2 {
    public class Node {
        public  Node next = null;
        public int data;

        public Node(int d) {
            this.data = d;
        }

        public void AppendToTail(int d) {
            Node end = new Node(d);
            Node n = this;
            while(n.next != null) {
                n = n.next;
            }
            n.next = end;
        }

        private Node DeleteNode(Node head, int d) {
            if (head == null) { return null; }

            Node n = head;

            if (n.data == d) {
                return head.next; // Moved head
            }

            while (n.next != null) {
                if (n.next.data == d) {
                    n.next = n.next.next;
                    return head; // No change
                }
                n = n.next;
            }
            return head;
        }
    }
}
