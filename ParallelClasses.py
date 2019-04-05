import multiprocessing as mp
import SurvivalModelClasses as Cls
from MultiSurvivalModelClasses import MultiCohort

MAX_PROCESSES = mp.cpu_count()  # maximum number of threads


def pool_function(cohort, n_time_steps):
    """
    :param cohort:
    :param n_time_steps:
    :return: cohort after being simulated
    """

    cohort.simulate(n_time_steps)
    return cohort


class ParallelMultiCohort(MultiCohort):

    def __init__(self, ids, pop_sizes, mortality_probs):
        """
        :param ids: (list) of ids for cohorts to simulate
        :param pop_sizes: (list) of population sizes of cohorts to simulate
        :param mortality_probs: (list) of the mortality probabilities
        """

        MultiCohort.__init__(self, ids, pop_sizes, mortality_probs)
        self.cohorts = []

        for i in range(len(self.ids)):
            # create a cohort
            self.cohorts.append(
                Cls.Cohort(id=self.ids[i], pop_size=self.popSizes[i], mortality_prob=self.mortalityProbs[i]))

    def simulate(self, n_time_steps, n_processes=MAX_PROCESSES):

        # create a list of arguments for simulating the cohorts in parallel
        starmap_args = [(cohort, n_time_steps) for cohort in self.cohorts]

        # simulate all cohorts in parallel
        with mp.Pool(n_processes) as pl:
            simulated_cohorts = pl.starmap(pool_function, starmap_args)

        # outcomes from simulating all cohorts
        for cohort in simulated_cohorts:
            self.multiCohortOutcomes.extract_outcomes(cohort)

        # calculate the summary statistics of from all cohorts
        self.multiCohortOutcomes.calculate_summary_stats()