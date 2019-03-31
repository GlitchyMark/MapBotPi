#include <iostream>
#include "robot.h"

using namespace std;
namespace MapBotPi {

int main() {
    Robot r;

    cout << "MapBot Initiated." << endl;
    while (r.update() == true);

    return 0;
}

}   // namespace MapBotPi