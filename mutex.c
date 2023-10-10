#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t condition[3] = {PTHREAD_COND_INITIALIZER};

int count = 0;

void *printThreadID(void *arg) {
    char id = *(char *)arg;
    int target = 1000;

    for (int i = 0; i < target; ++i) {
        pthread_mutex_lock(&mutex);
        while (id - 'A' != (count + 1) % 3) {
            pthread_cond_wait(&condition[id - 'A'], &mutex);
        }
        printf("%c", id);
        count++;
        pthread_cond_signal(&condition[(count + 1) % 3]);
        pthread_mutex_unlock(&mutex);
    }

    return NULL;
}

int main() {
    pthread_t threadA, threadB, threadC;
    char idA = 'A', idB = 'B', idC = 'C';

    pthread_create(&threadA, NULL, printThreadID, (void *)&idA);
    pthread_create(&threadB, NULL, printThreadID, (void *)&idB);
    pthread_create(&threadC, NULL, printThreadID, (void *)&idC);

    pthread_join(threadA, NULL);
    pthread_join(threadB, NULL);
    pthread_join(threadC, NULL);

    printf("\n");

    return 0;
}
