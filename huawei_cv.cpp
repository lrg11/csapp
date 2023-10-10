/*
//有惊群现象
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
int currentThread = 0; // 当前应该执行的线程编号

#define CNT 1000

void printId(const char id, int threadNum) {
    for (int i = 0; i < CNT; ++i) {
        std::unique_lock<std::mutex> lock(mtx);
        
        // 检查当前线程是否应该执行，如果不是则等待
        while (currentThread != threadNum) {
            cv.wait(lock);
        }
        
        // 打印ID
        std::cout << id;
        
        // 更新当前线程编号，循环执行ABC
        currentThread = (currentThread + 1) % 3;
        
        // 通知下一个线程可以执行
        cv.notify_all();
    }
}

int main() {
    std::thread threadA(printId, 'A', 0);
    std::thread threadB(printId, 'B', 1);
    std::thread threadC(printId, 'C', 2);
    
    threadA.join();
    threadB.join();
    threadC.join();
    
    std::cout << std::endl;
    
    return 0;
}
*/


//解决惊群现象
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv[3]; // 为每个线程创建一个条件变量
int count = 0;  // 用于跟踪当前应该输出的线程
int currentThread = 0; // 用于指示当前应该执行的线程

void printThreadID(char id, int target, int threadIndex) {
    for (int i = 0; i < target; ++i) {
        std::unique_lock<std::mutex> lock(mtx);
        cv[threadIndex].wait(lock, [threadIndex]() { return threadIndex == (currentThread + 1) % 3; });
        std::cout << id;
        count++;
        currentThread = (currentThread + 1) % 3; // 更新当前应该执行的线程
        cv[(currentThread + 1) % 3].notify_one(); // 唤醒下一个线程
    }
}

int main() {
    int target = 1000; // 控制每个线程输出的次数
    
    std::thread threadA(printThreadID, 'A', target, 0);
    std::thread threadB(printThreadID, 'B', target, 1);
    std::thread threadC(printThreadID, 'C', target, 2);
    
    // 初始化，开始由线程A执行
    cv[1].notify_one();
    
    threadA.join();
    threadB.join();
    threadC.join();
    
    std::cout << std::endl; // 输出换行符以完成输出
    
    return 0;
}



/*
// 互斥锁
#include <iostream>
#include <thread>
#include <mutex>

std::mutex mtx; // 用于控制输出的互斥锁
int count = 0;  // 用于跟踪当前应该输出的线程

void printThreadID(char id, int target) {
    for (int i = 0; i < target; ++i) {
        std::unique_lock<std::mutex> lock(mtx);
        while (id - 'A' != count % 3) {
            // 如果不是轮到当前线程输出，则等待
            lock.unlock();
            std::this_thread::yield(); // 让出CPU时间片
            lock.lock();
        }
        std::cout << id;
        count++;
        lock.unlock();
    }
}

int main() {
    int target = 1000; // 控制每个线程输出的次数
    
    std::thread threadA(printThreadID, 'A', target);
    std::thread threadB(printThreadID, 'B', target);
    std::thread threadC(printThreadID, 'C', target);
    
    threadA.join();
    threadB.join();
    threadC.join();
    
    std::cout << std::endl; // 输出换行符以完成输出
    
    return 0;
}
*/