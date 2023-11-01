from .ride_state import RideState


class Ride:
    _state = None

    def __init__(self, state: RideState) -> None:
        self.transition_to(state)

    def transition_to(self, state: RideState) -> None:
        self._state = state
        self._state.ride = self

    def accept(self) -> None:
        self._state.accept()

    def start(self) -> None:
        self._state.start()

    def end(self) -> None:
        self._state.end()

    def cancel(self) -> None:
        self._state.cancel()
