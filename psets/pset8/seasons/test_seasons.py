from datetime import date
from seasons import calc_minutes, format_output

def test_calc():
    assert calc_minutes(date(2023, 2, 17)) == 525600
    assert calc_minutes(date(2022, 2, 17)) == 1051200

def test_format():
    assert format_output(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert format_output(1051200) == "One million, fifty-one thousand, two hundred minutes"
