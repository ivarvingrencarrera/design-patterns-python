from unittest import TestCase

from .ride import Ride
from .ride_state import (
    InvalidOperationError,
    RideAccepted,
    RideCanceled,
    RideEnded,
    RideRequested,
    RideStarted,
)


class TestRide(TestCase):
    def setUp(self) -> None:
        self.ride = Ride(RideRequested())

    def tearDown(self) -> None:
        del self.ride

    def test_requested_to_accepted(self) -> None:
        self.ride.accept()
        self.assertIsInstance(self.ride._state, RideAccepted)

    def test_requested_to_canceled(self) -> None:
        self.ride.cancel()
        self.assertIsInstance(self.ride._state, RideCanceled)

    def test_requested_to_started(self) -> None:
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.start()
        self.assertEqual(str(err.exception), 'Requested ride cannot be started')

    def test_requested_to_ended(self) -> None:
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.end()
        self.assertEqual(str(err.exception), 'Requested ride cannot be ended')

    def test_accepted_to_started(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.assertIsInstance(self.ride._state, RideStarted)

    def test_accepted_to_canceled(self) -> None:
        self.ride.accept()
        self.ride.cancel()
        self.assertIsInstance(self.ride._state, RideCanceled)

    def test_accepted_to_accepted(self) -> None:
        self.ride.accept()
        with self.assertRaises(InvalidOperationError):
            self.ride.accept()

    def test_accepted_to_ended(self) -> None:
        self.ride.accept()
        with self.assertRaises(InvalidOperationError):
            self.ride.end()

    def test_started_to_ended(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.ride.end()
        self.assertIsInstance(self.ride._state, RideEnded)

    def test_started_to_accepted(self) -> None:
        self.ride.accept()
        self.ride.start()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.accept()
        self.assertEqual(str(err.exception), 'Started ride cannot be accepted')

    def test_started_to_started(self) -> None:
        self.ride.accept()
        self.ride.start()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.start()
        self.assertEqual(str(err.exception), 'Started ride cannot be started again')

    def test_started_to_canceled(self) -> None:
        self.ride.accept()
        self.ride.start()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.cancel()
        self.assertEqual(str(err.exception), 'Started ride cannot be canceled')

    def test_ended_to_accepted(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.ride.end()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.accept()
        self.assertEqual(str(err.exception), 'Ended ride cannot be accepted')

    def test_ended_to_started(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.ride.end()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.start()
        self.assertEqual(str(err.exception), 'Ended ride cannot be started')

    def test_ended_to_ended(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.ride.end()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.end()
        self.assertEqual(str(err.exception), 'Ended ride cannot be ended again')

    def test_ended_to_canceled(self) -> None:
        self.ride.accept()
        self.ride.start()
        self.ride.end()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.cancel()
        self.assertEqual(str(err.exception), 'Ended ride cannot be canceled')

    def test_canceled_to_accepted(self) -> None:
        self.ride.cancel()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.accept()
        self.assertEqual(str(err.exception), 'Canceled ride cannot be accepted')

    def test_canceled_to_started(self) -> None:
        self.ride.cancel()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.start()
        self.assertEqual(str(err.exception), 'Canceled ride cannot be started')

    def test_canceled_to_ended(self) -> None:
        self.ride.cancel()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.end()
        self.assertEqual(str(err.exception), 'Canceled ride cannot be ended')

    def test_canceled_to_canceled(self) -> None:
        self.ride.cancel()
        with self.assertRaises(InvalidOperationError) as err:
            self.ride.cancel()
        self.assertEqual(str(err.exception), 'Canceled ride cannot be canceled again')
