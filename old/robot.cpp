#include <string>
#include <vector>

#include "include/serial/serial.h"
#include "include/rapidjson/document.h"
#include "robot.h"
#include "serial_cfg.h"

using std::string;
namespace MapBotPi {
Robot::Robot() {
    serial::Serial mv_left(MV_LEFT_PORT, BAUD_RATE);
    serial::Serial mv_right(MV_RIGHT_PORT, BAUD_RATE);
    serial::Serial motor_driver(MOTOR_DRIVER_PORT, BAUD_RATE);

    mv_left.open();
    mv_right.open();
    motor_driver.open();
}

Robot::~Robot() {
    mv_left.close();
    mv_right.close();
    motor_driver.close();
}

bool Robot::update() {
    // UpdatePosition();
    UpdateState();
    Execute();
}

void Robot::UpdatePosition() {
    /* recieve serial data from
    cameras, update the map */

    mv_left.write("s");
    string left_data = mv_left.readline();
    mv_right.write("s");
    string right_data = mv_right.readline();

    
}

void Robot::UpdateState() {
    /* update the state variable
    based on the position and
    time */

    state = STATE_DEBUG;
}

void Robot::Execute() {
    ResponseBuffer r;
    MessageList messages = LogicStateMachine();     // this is where all the game logic happens

    for (MessageList::iterator i = messages.begin(); i != messages.end(); i++)  {
        motor_driver.write(*i);
        r.push_back(motor_driver.readline());
    }

    responses.empty();
    responses = r;
}

Robot::MessageList Robot::LogicStateMachine() {
    switch (state) {
        default: case STATE_FOLLOW_CIRCLE:
            return MessageList();   // update later
        case STATE_RETRIEVE_CUBE:
            return MessageList();   // update later
        case STATE_HIT_BY_OPPONENT:
            return MessageList();   // update later
        case STATE_ENDGAME:
            return MessageList();   // update later
        case STATE_DEBUG:
            return Debug();
    }
}

Robot::MessageList Robot::Debug() {
    
}

}   // namespace MapBotPi