using System;
using System.Collections.Generic;

namespace csharp.Chapter2 {
    public class Node {
        public Node next = null;
        public int data;

        public Node(Node next, int data) {
            this.next = next;
            this.data = data;
        }
    }
}
