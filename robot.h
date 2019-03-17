#pragma once

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
}