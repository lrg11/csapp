#include <iostream>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

sem_t sem;

// 进程函数
void* process(void* arg) {
    int pid = *(int*)arg;
    cout << "Process " << pid << " starts running." << endl;
    sleep(2);
    cout << "Process " << pid << " ends running." << endl;
    return NULL;
}

// 线程函数
void* thread(void* arg) {
    int tid = *(int*)arg;
    cout << "Thread " << tid << " starts running." << endl;
    sleep(1);
    cout << "Thread " << tid << " ends running." << endl;
    return NULL;
}

// 协程函数
void* coroutine(void* arg) {
    int pid = *(int*)arg;
    cout << "Coroutine " << pid << " starts running." << endl;
    sleep(1);
    //sem_wait(&sem);
    cout << "Coroutine " << pid << " yields." << endl;
    sem_post(&sem); // 释放信号量
   // sleep(1);
    cout << "Coroutine " << pid << " resumes running." << endl;
    return NULL;
}

int main() {
    int n = 10; // 进程、线程和协程的数量
    pthread_t threads[n];
    int threadArgs[n];
    int coroutineArgs[n];
    

    // 初始化信号量并设置为0
    sem_init(&sem, 0, 0);

    // 创建进程
    for (int i = 0; i < n; i++) {
        threadArgs[i] = i;
        if (fork() == 0) { // 子进程
            process(&threadArgs[i]);
            exit(0);
        }
    }

    // 等待所有子进程结束
    for (int i = 0; i < n; i++) {
        wait(NULL);
    }

    // 创建线程
    for (int i = 0; i < n; i++) {
        coroutineArgs[i] = i;
        pthread_create(&threads[i], NULL, thread, &coroutineArgs[i]);
    }
    for (int i = 0; i < n; i++) { // 等待线程结束
        pthread_join(threads[i], NULL);
    }

    // 创建协程
    for (int i = 0; i < n; i++) {
        coroutineArgs[i] = i;
        pthread_create(&threads[i], NULL, coroutine, &coroutineArgs[i]);
    }
    for (int i = 0; i < n ; i++) {
        sem_wait(&sem); // 等待所有协程释放信号量
    }
    for (int i = 0; i < n; i++) { // 等待协程结束
        pthread_join(threads[i], NULL);
    }

    return 0;
}
