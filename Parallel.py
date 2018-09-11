import SurvivalModelClasses as Cls
import multiprocessing as mp

MAX_PROCESSES = mp.cpu_count()  # maximum number of threads


def pool_function(cohort, n_time_steps):
    """
    :param cohort:
    :param n_time_steps:
    :return: cohort after being simulated
    """

    cohort.simulate(n_time_steps)
    return cohort


class ParallelMultiCohort(Cls.MultiCohort):

    def simulate(self, n_time_steps, n_processes=MAX_PROCESSES):

        # create a list of arguments for simulating the cohorts in parallel
        starmap_args = [(cohort, n_time_steps) for cohort in self.cohorts]

        # simulate all cohorts in parallel
        with mp.Pool(n_processes) as pl:
            simulated_cohorts = pl.starmap(pool_function, starmap_args)

        # outcomes from simulating all cohorts
        self.multiCohortOutcomes.extract_outcomes(simulated_cohorts)
