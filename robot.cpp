#include "robot.h"

Robot::Robot() {
    /* intialization stuff goes here */ 
}

bool Robot::update() {
    UpdatePosition();
    UpdateState();
    Execute();
}

void Robot::UpdatePosition() {
    /* recieve serial data from
    cameras, update the map */
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