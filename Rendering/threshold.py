class Threshold:
    def __init__(self, millisecond_threshold: int):
        self.threshold = millisecond_threshold
        self.milliseconds = 0

    def is_threshold_exceeded(self, milliseconds_elapsed: int) -> bool:
        """
        This function will add the elapses seconds on to the internal timer, then check if the
        threshold is exceeded.
        If it is exceeded, it will decrement the counter by one threshold and return true.
        No matter how far the threshold is exceeded, the counter can only be decremented by one
        threshold value.
        """
        self.milliseconds += milliseconds_elapsed
        if self.milliseconds > self.threshold:
            self.milliseconds -= self.threshold
            return True
        return False
