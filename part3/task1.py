def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        "expected {}, got {}".format(expected_result, actual_result)


def main():
    test_input_text(8, 8)
    test_input_text(8, 11)


if __name__ == "__main__":
    main()
