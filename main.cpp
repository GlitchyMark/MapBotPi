#include <iostream>
#include "robot.h"

using namespace std;

int main() {
    Robot r;

    cout << "MapBot Initiated." << endl;
    while (r.update() == true);

    return 0;
}