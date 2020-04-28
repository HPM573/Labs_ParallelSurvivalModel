import multiprocessing as mp
from SurvivalModelClasses import Cohort
from MultiSurvivalModelClasses import MultiCohort

MAX_PROCESSES = mp.cpu_count()  # maximum number of processors


def simulate_this_cohort(cohort, n_time_steps):
    """
    :param cohort: a cohort of patients
    :param n_time_steps: simulation length
    :return: cohort after being simulated
    """

    # simulate and return the cohort
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

        # create cohorts
        for i in range(len(self.ids)):
            self.cohorts.append(Cohort(id=self.ids[i],
                                       pop_size=self.popSizes[i],
                                       mortality_prob=self.mortalityProbs[i])
                                )

    def simulate(self, n_time_steps, n_processes=MAX_PROCESSES):

        # create a list of arguments for simulating the cohorts in parallel

        # simulate all cohorts in parallel

        # outcomes from simulating all cohorts
        for cohort in simulated_cohorts:
            self.multiCohortOutcomes.extract_outcomes(cohort)

        # calculate the summary statistics of from all cohorts
        self.multiCohortOutcomes.calculate_summary_stats()
