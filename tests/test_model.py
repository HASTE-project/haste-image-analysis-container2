import datetime

from haste.image_analysis_container2.kendall_tau_model import KendallTauInterestingnessModel


def test_instantiation():
    # Test we can instantiate the model (there is no mongodb available for the travis CI)

    initials = 'deleteme'
    stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '__' + initials

    print(stream_id)

    model = KendallTauInterestingnessModel(5)  # window length
