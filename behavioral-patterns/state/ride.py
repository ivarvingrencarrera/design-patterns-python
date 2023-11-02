from .ride_state import RideState


class Ride:
    _ride_state = None

    def __init__(self, ride_state: RideState) -> None:
        self.transition_to(ride_state)

    def transition_to(self, ride_state: RideState) -> None:
        self._ride_state = ride_state
        self._ride_state.ride = self

    def accept(self) -> None:
        self._ride_state.accept()

    def start(self) -> None:
        self._ride_state.start()

    def end(self) -> None:
        self._ride_state.end()

    def cancel(self) -> None:
        self._ride_state.cancel()
