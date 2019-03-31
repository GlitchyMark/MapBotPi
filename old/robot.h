#pragma once

#include <vector>
#include <string>
#include "include/serial/serial.h"
#include "include/rapidjson/document.h"

namespace MapBotPi {

class Robot {

    public:
        Robot(void);
        ~Robot(void);
        bool update(void);

        void UpdatePosition(void);
        void UpdateState(void);
        void Execute(void);

    private:
        typedef enum {
            STATE_FOLLOW_CIRCLE,
            STATE_RETRIEVE_CUBE,
            STATE_HIT_BY_OPPONENT,
            STATE_ENDGAME,
            STATE_DEBUG
        } GameState;
        typedef std::vector<std::string> MessageList;
        typedef std::vector<std::string> ResponseBuffer;

        MessageList LogicStateMachine(void);
        MessageList FollowCircle(void);
        MessageList RetrieveCube(void);
        MessageList HitByOpponent(void);
        MessageList Endgame(void);
        MessageList Debug(void);

        
        long current_time;
        GameState state;
        ResponseBuffer responses;

        serial::Serial mv_left;
        serial::Serial mv_right;
        serial::Serial motor_driver;

        rapidjson::Document left_json;
        rapidjson::Document right_json;
};

}   // namespace MapBotPi