using System;
using System.Collections.Generic;
using csharp.Chapter2;

namespace csharp.Chapter2 {
    /// Remove Dups:  Write code to remove duplicated from an unsorted linked list.
    
    public class TwoOne {
        public LinkedList linkedList = new LinkedList();

        public TwoOne() {
            Console.WriteLine("Question 2.1");
        }

        public void CreateTestData() {
            // 0, 2, 4, 6, 6, 2, 8, 0, 0, 6, 4, 2
            // Correct output should be:  0, 2, 4, 6, 8
            linkedList.InsertAtBeginning(0);
            linkedList.InsertAtEnd(2);
            linkedList.InsertAtEnd(4);
            linkedList.InsertAtEnd(6);
            linkedList.InsertAtEnd(6);
            linkedList.InsertAtEnd(2);
            linkedList.InsertAtEnd(8);
            linkedList.InsertAtEnd(0);
            linkedList.InsertAtEnd(0);
            linkedList.InsertAtEnd(6);
            linkedList.InsertAtEnd(4);
            linkedList.InsertAtEnd(2);
        }

        public void DoTheThings() {
            this.linkedList.Print();
            this.linkedList.InsertAtIndex(4, 46);
            this.linkedList.Print();
        }
    }
}
