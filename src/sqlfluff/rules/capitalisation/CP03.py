"""Implementation of Rule CP03."""

from typing import List, Tuple
from sqlfluff.core.rules.crawlers import SegmentSeekerCrawler

from sqlfluff.rules.capitalisation.CP01 import Rule_CP01


class Rule_CP03(Rule_CP01):
    """Inconsistent capitalisation of function names.

    **Anti-pattern**

    In this example, the two ``SUM`` functions don't have the same capitalisation.

    .. code-block:: sql

        SELECT
            sum(a) AS aa,
            SUM(b) AS bb
        FROM foo

    **Best practice**

    Make the case consistent.

    .. code-block:: sql

        SELECT
            sum(a) AS aa,
            sum(b) AS bb
        FROM foo

    """

    name = "capitalisation.functions"
    aliases = ("L030",)
    is_fix_compatible = True

    crawl_behaviour = SegmentSeekerCrawler(
        {"function_name_identifier", "bare_function"}
    )
    _exclude_elements: List[Tuple[str, str]] = []
    config_keywords = [
        "extended_capitalisation_policy",
        "ignore_words",
        "ignore_words_regex",
    ]
    _description_elem = "Function names"

    def _get_fix(self, segment, fixed_raw):
        return super()._get_fix(segment, fixed_raw)
