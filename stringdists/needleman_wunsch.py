import numpy as np

class SimilarityMeasure(object):
    pass

def sim_ident(char1, char2):
    return int(char1 == char2)


class NeedlemanWunsch(SimilarityMeasure):
    """Computes Needleman-Wunsch measure.

    The Needleman-Wunsch distance generalizes the Levenshtein distance and considers global alignment between two strings.
    Specifically, it is computed by assigning a score to each alignment between the two input strings and choosing the
    score of the best alignment, that is, the maximal score. An alignment between two strings is a set of correspondences
    between their characters, allowing for gaps.

    Args:
        gap_cost (float): Cost of gap (defaults to 2.0).
        sim_func (function): Similarity function to give a score for each correspondence between the characters (defaults
                             to an identity function, which returns 2 if the two characters are the same and 0 otherwise.

    Attributes:
        gap_cost (float): An attribute to store the gap cost.
        sim_func (function): An attribute to store the similarity function.
    """

    def __init__(self, gap_cost=2.0, sim_func=sim_ident):
        self.gap_cost = gap_cost
        self.sim_func = sim_func
        super(NeedlemanWunsch, self).__init__()

    def get_raw_score(self, string1, string2):
        """Computes the raw Needleman-Wunsch score between two strings.

        Args:
            string1,string2 (str) : Input strings.

        Returns:
            Needleman-Wunsch similarity score (float).

        Raises:
            TypeError : If the inputs are not strings or if one of the inputs is None.

        Examples:
            >>> nw = NeedlemanWunsch()
            >>> nw.get_raw_score('dva', 'deeva')
            1.0
            >>> nw = NeedlemanWunsch(gap_cost=0.0)
            >>> nw.get_raw_score('dva', 'deeve')
            2.0
            >>> nw = NeedlemanWunsch(gap_cost=1.0, sim_func=lambda s1, s2 : (2.0 if s1 == s2 else -1.0))
            >>> nw.get_raw_score('dva', 'deeve')
            1.0
            >>> nw = NeedlemanWunsch(gap_cost=0.5, sim_func=lambda s1, s2 : (1.0 if s1 == s2 else -1.0))
            >>> nw.get_raw_score('GCATGCUA', 'GATTACA')
            2.5
        """

        dist_mat = np.zeros((len(string1) + 1, len(string2) + 1),
                            dtype=np.float)

        # DP initialization
        for i in range(len(string1) + 1):
            dist_mat[i, 0] = -(i * self.gap_cost)

        # DP initialization
        for j in range(len(string2) + 1):
            dist_mat[0, j] = -(j * self.gap_cost)

        # Needleman-Wunsch DP calculation
        for i in range(1, len(string1) + 1):
            for j in range(1, len(string2) + 1):
                match = dist_mat[i - 1, j - 1] + self.sim_func(string1[i - 1],
                                                               string2[j - 1])
                delete = dist_mat[i - 1, j] - self.gap_cost
                insert = dist_mat[i, j - 1] - self.gap_cost
                dist_mat[i, j] = min(match, delete, insert)

        return dist_mat[dist_mat.shape[0] - 1, dist_mat.shape[1] - 1]

    def get_gap_cost(self):
        """Get gap cost.

        Returns:
            Gap cost (float).
        """
        return self.gap_cost

    def get_sim_func(self):
        """Get the similarity function.

        Returns:
            similarity function (function).
        """
        return self.sim_func

    def set_gap_cost(self, gap_cost):
        """Set gap cost.

        Args:
            gap_cost (float): Cost of gap.
        """
        self.gap_cost = gap_cost
        return True

    def set_sim_func(self, sim_func):
        """Set similarity function.

        Args:
            sim_func (function): Similarity function to give a score for the correspondence between characters.
        """
        self.sim_func = sim_func
        return True
