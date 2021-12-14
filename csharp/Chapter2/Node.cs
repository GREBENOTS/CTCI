using System;
namespace csharp.Chapter2 {
    public class Node {
        private Node next = null;
        private int data;

        public Node(int d) {
            this.data = d;
        }

        private void AppendToTail(int d) {
            Node end = new(d);
            Node n = this;
            while(n.next != null) {
                n = n.next;
            }
            n.next = end;
        }
    }
}
