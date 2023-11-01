from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .ride_exception import InvalidOperationError

if TYPE_CHECKING:   # pragma: no cover
    from .ride import Ride


class RideState(ABC):
    @property
    def ride(self) -> Ride:
        return self._ride

    @ride.setter
    def ride(self, ride: Ride) -> None:
        self._ride = ride

    @abstractmethod
    def accept(self) -> None:
        pass

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def end(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass


class RideEnded(RideState):
    def accept(self) -> None:
        raise InvalidOperationError('Ended', 'accepted')

    def start(self) -> None:
        raise InvalidOperationError('Ended', 'started')

    def end(self) -> None:
        raise InvalidOperationError('Ended', 'ended again')

    def cancel(self) -> None:
        raise InvalidOperationError('Ended', 'canceled')


class RideCanceled(RideState):
    def accept(self) -> None:
        raise InvalidOperationError('Canceled', 'accepted')

    def start(self) -> None:
        raise InvalidOperationError('Canceled', 'started')

    def end(self) -> None:
        raise InvalidOperationError('Canceled', 'ended')

    def cancel(self) -> None:
        raise InvalidOperationError('Canceled', 'canceled again')


class RideStarted(RideState):
    def accept(self) -> None:
        raise InvalidOperationError('Started', 'accepted')

    def start(self) -> None:
        raise InvalidOperationError('Started', 'started again')

    def end(self) -> None:
        self.ride.transition_to(RideEnded())

    def cancel(self) -> None:
        raise InvalidOperationError('Started', 'canceled')


class RideAccepted(RideState):
    def accept(self) -> None:
        raise InvalidOperationError('Accepted', 'accepted again')

    def start(self) -> None:
        self.ride.transition_to(RideStarted())

    def end(self) -> None:
        raise InvalidOperationError('Accepted', 'ended')

    def cancel(self) -> None:
        self.ride.transition_to(RideCanceled())


class RideRequested(RideState):
    def accept(self) -> None:
        self.ride.transition_to(RideAccepted())

    def start(self) -> None:
        raise InvalidOperationError('Requested', 'started')

    def end(self) -> None:
        raise InvalidOperationError('Requested', 'ended')

    def cancel(self) -> None:
        self.ride.transition_to(RideCanceled())
