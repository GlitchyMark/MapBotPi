#pragma once

#include "include/serial/serial.h"
#include "include/rapidjson/document.h"

class Robot {

    public:
        Robot(void);
        bool update(void);

        void UpdatePosition(void);
        void UpdateState(void);
        void Execute(void);

    private:
        typedef enum {
            STATE_FOLLOW_CIRCLE,
            STATE_RETRIEVE_CUBE,
            STATE_HIT_BY_OPPONENT,
            STATE_ENDGAME
        } GameState;
        
        long current_time;
        GameState state;

        serial::Serial mv_left;
        serial::Serial mv_right;
        serial::Serial motor_driver;

        rapidjson::Document left_json;
        rapidjson::Document right_json;
}