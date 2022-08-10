from datetime import datetime

import pytest


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    month =  int(pesel[2:4])
    year = '19'
    if month > 20:
        year = '20'
        month -= 20
    birth_date = datetime(int(year + pesel[0: 2]),month, int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]) and len(pesel) == 11,
        "gender": gender,
        "birth_date": birth_date
    }
    return result


@pytest.mark.parametrize('pesel',
                         ['46102074721', '50050281191', '48072396841', '44031693282', '39080913953', '00102114128',
                          '10041793568', '30062622131', '82021198184', '37122999152'])
def test_ap_pesel(pesel):
    assert analyze_pesel(pesel)['pesel'] == pesel

@pytest.mark.parametrize('pesel',
                         ['46102074721', '50050281191', '48072396841', '44031693282', '39080913953', '00102114128',
                          '10041793568', '30062622131', '82021198184', '37122999152'])
def test_ap_valid(pesel):
    assert analyze_pesel(pesel)['valid']

@pytest.mark.parametrize('pesel',
                         ['46102074722', '50050281192', '48072396842', '44031693283', '39080913954', '00102114129',
                          '10041793569', '30062622132', '82021198185', '37122999153'])
def test_ap_invalid(pesel):
    assert not analyze_pesel(pesel)['valid']


@pytest.mark.parametrize('pesel, gender',
                         (
                                 ('46102074721', 'female'),
                                 ('50050281191', 'male'),
                                 ('48072396841', 'female'),

                         )
)
def test_ap_gender(pesel, gender):
    assert analyze_pesel(pesel)['gender'] == gender


@pytest.mark.parametrize('pesel, date',
                         (('46102074722', datetime(1946, 10,20)),
                          ('50050281192', datetime(1950, 5,2)),
                         ('30220357589', datetime(2030, 2, 3)))
                         )
def test_ap_invalid(pesel, date):
    assert  analyze_pesel(pesel)['birth_date'] == date
