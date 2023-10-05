from hexlet_pytest.example import reverse


def test_reverse():
    print(reverse("Hex"))
    assert reverse('Hexlet') == 'TelxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''
