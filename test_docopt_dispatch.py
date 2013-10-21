from pytest import raises, yield_fixture as fixture

from docopt_dispatch import Dispatch, DispatchError


class OptionMarker(Exception):
    pass


class ArgumentMarker(Exception):
    pass


@fixture
def dispatch():
    dispatch = Dispatch()

    @dispatch.on('--option')
    def option(**kwargs):
        raise OptionMarker(kwargs)

    @dispatch.on('<argument>')
    def argument(**kwargs):
        raise ArgumentMarker(kwargs)

    yield dispatch


def test_dispatch_can_dispatch_on_option(dispatch):
    with raises(OptionMarker) as error:
        dispatch('usage: prog [--option] [<argument>]', '--option')
    assert error.value.message == {'option': True, 'argument': None}


def test_dispatch_can_dispatch_on_argument(dispatch):
    with raises(ArgumentMarker) as error:
        dispatch('usage: prog [--option] [<argument>]', 'hi')
    assert error.value.message == {'option': False, 'argument': 'hi'}


def test_dispatch_will_raise_error_if_it_cannot_dispatch(dispatch):
    with raises(DispatchError) as error:
        dispatch('usage: prog [--option] [<argument>]', '')
    message = 'None of dispatch conditions (--option, <argument>) is triggered'
    assert error.value.message == message
