public class mutex {
    private static final Object lock = new Object();
    private static int count = 0;

    public static void main(String[] args) {
        int target = 1000;

        Thread threadA = new Thread(() -> printThreadID('A', target));
        Thread threadB = new Thread(() -> printThreadID('B', target));
        Thread threadC = new Thread(() -> printThreadID('C', target));

        threadA.start();
        threadB.start();
        threadC.start();

        try {
            threadA.join();
            threadB.join();
            threadC.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println();
    }

    private static void printThreadID(char id, int target) {
        for (int i = 0; i < target; i++) {
            synchronized (lock) {
                while (id - 'A' != (count + 1) % 3) {
                    try {
                        lock.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print(id);
                count++;
                lock.notifyAll();
            }
        }
    }
}
