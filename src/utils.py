# Build: 213eb411067efa5a15b9dbe8a2aff28a

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
