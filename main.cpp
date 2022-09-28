// 2022 Qi Luo U85845640
// 2022 Quang Luan Dang Tran (Dan) U12XXXXXX

// We Choose Dan's BUid

#include <iostream>
#include <string>

using namespace std;

const string states[12];

int state_1 = 0;
int state_0 = 0;
int in0 = 1;
int next_state_1;
int next_state_0;

int and_comparetor(int x, int y) {
    if (x == 0 && y == 0) {
        return 0;
    } else {
        return 1;
    }
}

int or_comparetor(int x, int y) {
    if (x == 1 && y == 1) {
        return 1;
    } else {
        return 0;
    }
}

int not_comparetor(int x) {
    if (x == 1) {
        return 0;
    } else {
        return 1;
    }
}

void state_machine() {
    printf("state_1 = %d\n", state_1);
    printf("state_0 = %d\n", state_0);
    next_state_1 = and_comparetor(in0, state_0);
    next_state_0 = not_comparetor(in0);
    printf("next_state_1 = %d\n", next_state_1);
    printf("next_state_0 = %d\n", next_state_0);
    state_1 = next_state_1;
    state_0 = next_state_0;
};

int main() {    
    bool x = false;
    for (int i=0; i < 12; i++) {
        printf("Step %d\n", i+1);
        state_machine();
    }
    if (state_1 == 1 && state_0 == 0) {
        x = true;
    }
    printf("%s\n", x?"true":"false");
    return 0;
}

