import pytest

from controller.cron_controller import CronController


def test_valid_cron_exp_all_wildcards():
    assert (CronController().evaluate(
        "* * * * * abc")) == ("minute        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 "
                              "28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 "
                              "57 58 59\nhour          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 "
                              "23\nday of month  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 "
                              "27 28 29 30 31\nmonth         1 2 3 4 5 6 7 8 9 10 11 12\nday of week   0 1 2 3 4 5 "
                              "6\noperations    abc")


def test_valid_cron_exp_one_wildcard():
    assert (CronController().evaluate(
        "* 1 1 1 1 abc")) == ("minute        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 "
                              "24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 "
                              "49 50 51 52 53 54 55 56 57 58 59\n"
                              "hour          1\n"
                              "day of month  1\n"
                              "month         1\n"
                              "day of week   1\n"
                              "operations    abc")


def test_valid_cron_exp():
    assert (CronController().evaluate(
        "* * * * * abc")) == ("minute        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 "
                              "28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 "
                              "57 58 59\nhour          0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 "
                              "23\nday of month  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 "
                              "27 28 29 30 31\nmonth         1 2 3 4 5 6 7 8 9 10 11 12\nday of week   0 1 2 3 4 5 "
                              "6\noperations    abc")


def test_valid_cron_exp_range_input():
    assert (CronController().evaluate(
        "1-20 1 1 1 1 abc")) == ("minute        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20\n"
                                 "hour          1\n"
                                 "day of month  1\n"
                                 "month         1\n"
                                 "day of week   1\n"
                                 "operations    abc")


def test_valid_cron_exp_list_separated_input():
    assert (CronController().evaluate(
        "1,2,3,4 1 1 1 1 abc")) == (('minute        1 2 3 4\n'
                                     'hour          1\n'
                                     'day of month  1\n'
                                     'month         1\n'
                                     'day of week   1\n'
                                     'operations    abc'))


def test_valid_cron_exp_step_values_input():
    assert (CronController().evaluate(
        "1/15 1 1 1 1 abc")) == ((('minute        0 15 30 45\n'
                                   'hour          1\n'
                                   'day of month  1\n'
                                   'month         1\n'
                                   'day of week   1\n'
                                   'operations    abc')))


def test_invalid_cron_exp_large_minute():
    assert (CronController().evaluate("62 * * * * abc")) is False


def test_invalid_cron_exp_large_hour():
    assert (CronController().evaluate("* 25 * * * abc")) is False


def test_invalid_cron_exp_invalid_cron_keyword():
    assert (CronController().evaluate("* a * * * abc")) is False


def test_invalid_cron_exp_invalid_cron_keyword_invalid_range():
    assert (CronController().evaluate("* 200-8 * * * abc")) is False
