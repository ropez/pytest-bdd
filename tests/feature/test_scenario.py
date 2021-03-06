"""Test scenario decorator."""
import pytest

from pytest_bdd import scenario
from pytest_bdd import exceptions


def test_scenario_not_found(request):
    """Test the situation when scenario is not found."""

    with pytest.raises(exceptions.ScenarioNotFound):
        scenario(
            'not_found.feature',
            'NOT FOUND'
        )


def test_scenario_comments(request):
    """Test comments inside scenario."""

    @scenario(
        'comments.feature',
        'Comments'
    )
    def test():
        pass

    test(request)
