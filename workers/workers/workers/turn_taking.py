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
    ALLOWED_TRANSITIONS = {
        InterviewState.IDLE: {
            InterviewState.PLAYING_QUESTION,
        },
        InterviewState.PLAYING_QUESTION: {
            InterviewState.WAITING_FOR_SPEECH,
        },
        InterviewState.WAITING_FOR_SPEECH: {
            InterviewState.LISTENING,
        },
        InterviewState.LISTENING: {
            InterviewState.TRANSCRIBING,
        },
        InterviewState.TRANSCRIBING: {
            InterviewState.NEXT_QUESTION,
        },
        InterviewState.NEXT_QUESTION: {
            InterviewState.PLAYING_QUESTION,
            InterviewState.COMPLETED,
        },
        InterviewState.COMPLETED: set(),
    }

    def __init__(self):
        self.state = InterviewState.IDLE

    def transition(self, new_state: InterviewState):
        if new_state not in self.ALLOWED_TRANSITIONS[self.state]:
            raise ValueError(
                f"Invalid transition: "
                f"{self.state.value} -> {new_state.value}"
            )

        print(f"[VOICE] {self.state.value} -> {new_state.value}")
        self.state = new_state
