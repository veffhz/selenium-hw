def test_substring(full_string, substring):
    assert substring in full_string, \
        "expected '{}' to be substring of '{}'".format(substring, full_string)


def main():
    test_substring("fulltext", "text")
    test_substring("fulltext", "some_value")


if __name__ == "__main__":
    main()
