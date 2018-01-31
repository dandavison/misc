public class Modulo {

    public static void _assert(Boolean cond, String msg) {
        if(!cond) {
            throw new AssertionError(msg);
        }
    }

    public static void main(String[] args) {
        int i;

        Modulo._assert(2 == 2, "something went wrong");

        for(i = -6; i < 7; i++) {
            System.out.println(i + "  " + Math.floorMod(i, 3));
        }
    }
}
