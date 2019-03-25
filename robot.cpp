#include <string>
#include <vector>

#include "include/serial/serial.h"
#include "include/rapidjson/document.h"
#include "robot.h"
#include "serial_cfg.h"

using std::string;

Robot::Robot() {
    serial::Serial mv_left(MV_LEFT_PORT, BAUD_RATE);
    serial::Serial mv_right(MV_RIGHT_PORT, BAUD_RATE);
    serial::Serial motor_driver(MOTOR_DRIVER_PORT, BAUD_RATE);
}

bool Robot::update() {
    UpdatePosition();
    UpdateState();
    Execute();
}

void Robot::UpdatePosition() {
    /* recieve serial data from
    cameras, update the map */
    uint8_t len[2];

    mv_left.write("s");
    mv_left.read(len, 2);
    string left_data = mv_left.read(len[1] << 8 | len[0]);
    mv_right.write("s");
    mv_right.read(len, 2);
    string right_data = mv_right.read(len[1] << 8 | len[0]);

    
}

void Robot::UpdateState() {
    /* update the state variable
    based on the position and
    time */
}

void Robot::Execute() {
    switch (state) {
        default: case STATE_FOLLOW_CIRCLE:
            break;
        case STATE_RETRIEVE_CUBE:
            break;
        case STATE_HIT_BY_OPPONENT:
            break;
        case STATE_ENDGAME:
            break;
    }
}