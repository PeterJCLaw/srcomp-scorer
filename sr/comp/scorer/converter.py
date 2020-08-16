from pathlib import Path
from typing import Type


class Converter:
    """
    Base class for converting between representations of a match's score.
    """

    @staticmethod
    def form_team_to_score(form, zone_id):
        """
        Prepare the part of the score dict for the given zone from the form data.
        """
        return {
            'zone': zone_id,
            'disqualified':
                form.get('disqualified_{}'.format(zone_id), None) is not None,
            'present':
                form.get('present_{}'.format(zone_id), None) is not None,
        }

    @classmethod
    def form_to_score(cls, match, form):
        """
        Prepare a score dict for the given match and form dict.

        This method is used to convert the submitted information for storage as
        YAML in the compstate.
        """
        zone_ids = range(len(match.teams))

        teams = {}
        for zone_id in zone_ids:
            tla = form.get('tla_{}'.format(zone_id), None)
            if tla:
                teams[tla] = cls.form_team_to_score(form, zone_id)

        zones = list(zone_ids) + ['other']
        arena = {}
        for zone in zones:
            arena[zone] = {'tokens': form.get('tokens_{}'.format(zone), '')}

        return {
            'arena_id': match.arena,
            'match_number': match.num,
            'teams': teams,
            'arena_zones': arena,
        }

    @staticmethod
    def score_to_form(score):
        """
        Prepare a form dict for the given score dict.

        This method is used when there is an existing score for a match.
        """
        form = {}

        for tla, info in score['teams'].items():
            zone_id = info['zone']
            form['tla_{}'.format(zone_id)] = tla
            form['disqualified_{}'.format(zone_id)] = info.get('disqualified', False)
            form['present_{}'.format(zone_id)] = info.get('present', True)

        for zone, info in score['arena_zones'].items():
            form['tokens_{}'.format(zone)] = info['tokens'].upper()

        return form

    @staticmethod
    def match_to_form(match: Match) -> Dict[str, Union[str, bool]]:
        """
        Prepare a fresh form dict for the given match.

        This method is used when there is no existing score for a match.
        """

        form = {}  # type: Dict[str, Union[str, bool]]

        for zone_id, tla in enumerate(match.teams):
            if tla:
                form['tla_{}'.format(zone_id)] = tla
                form['disqualified_{}'.format(zone_id)] = False
                form['present_{}'.format(zone_id)] = False

            form['tokens_{}'.format(zone_id)] = ''

        form['tokens'] = ''

        return form


def load_converter(compstate_path: Path) -> Type[Converter]:
    """
    Load the score coverter module from Compstate repo.

    :param Path compstate_path: The path to the compstate repo.
    """
    return Converter
