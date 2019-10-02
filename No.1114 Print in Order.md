### No.1114 Print in Order
* EMM是一个和线程相关的题，先大概心里有个数，线程相关的问题，primitive类型并不是线程安全的
```java
import java.util.concurrent.*;
class Foo {
    Semaphore run2, run3;

    public Foo() {
        run2 = new Semaphore(0);
        run3 = new Semaphore(0);
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        run2.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        run2.acquire();
        printSecond.run();
        run3.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        run3.acquire(); 
        printThird.run();
    }
}
```
