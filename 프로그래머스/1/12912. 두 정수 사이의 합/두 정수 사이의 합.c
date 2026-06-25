#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long long start = (a < b) ? a : b;
    long long end = (a > b) ? a : b;
    
    long long answer = (start + end) * (end - start + 1) / 2;
    
    return answer;
}