class _DLList<T> {

    private class Node {
        private T value;
        private Node next;
        private Node prev;
    }

    private Node first, last;
    private int size = 0;

    public void addFirst(T value) {
        Node node = new Node();
        node.value = value;
        node.next = first;
        if(first != null) {
            first.prev = node;
        }
        first = node;
        if(last == null) {
            last = first;
        }
        size++;
    }

    public void addLast(T value) {
        Node node = new Node();
        node.value = value;
        node.prev = last;
        if(last != null) {
            last.next = node;
        }
        last = node;
        if(first == null) {
            first = last;
        }
        size++;
    }

    public int size() {
        return size;
    }

    public void print() {
        Node ptr;
        ptr = first;
        while(ptr != null) {
            System.out.print(ptr.value + " ");
            ptr = ptr.next;
        }
        System.out.println();
    }
}


public class DLList {
    public static void main(String[] args) {
        _DLList<String> l = new _DLList<>();
        l.addFirst("bird");
        l.addFirst("fish");
        l.addLast("mammal");
        l.print();
    }
}
