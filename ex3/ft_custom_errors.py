#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def main() -> None:
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    try:
        raise PlantError("Tomato has wilted")
    except GardenError as e:
        print(f"Caught GardenError (via PlantError): {e}")


if __name__ == "__main__":
    main()
