from enum import Enum


class InterviewState(Enum):
    IDLE = "idle"
    PLAYING_QUESTION = "playing_question"
    WAITING_FOR_SPEECH = "waiting_for_speech"
    LISTENING = "listening"
    TRANSCRIBING = "transcribing"
    NEXT_QUESTION = "next_question"
    COMPLETED = "completed"


class TurnTakingStateMachine:
    def __init__(self):
        self.state = InterviewState.IDLE

    def transition(self, new_state: InterviewState):
        print(f"[VOICE] {self.state.value} -> {new_state.value}")
        self.state = new_state
