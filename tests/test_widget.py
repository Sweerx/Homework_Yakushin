from src.widget import mask_account_card


def test_mask_account_card_visa_platinum(visa_platinum_card):
    assert mask_account_card(visa_platinum_card) == mask_account_card(visa_platinum_card)

def test_mask_account_card_maestro(maestro_card):
    assert mask_account_card(maestro_card) == mask_account_card(maestro_card)

def test_mask_account_card_master(master_card):
    assert mask_account_card(master_card) == mask_account_card(master_card)

def test_mask_account_card_visa_classic(visa_classic_card, mask_visa_classic_card):
    assert mask_account_card(visa_classic_card) == mask_visa_classic_card