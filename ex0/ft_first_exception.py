#!/usr/bin/env python3

def test_temperature() -> None:
    print("Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C\n")

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
