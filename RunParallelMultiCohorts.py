import ParallelClasses as P
import SimPy.FigureSupport as Fig


MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length (years)
N_COHORTS = 500         # number of cohorts
COHORT_POP_SIZE = 100   # size of each cohort
ALPHA = 0.05            # significance level

if __name__ == '__main__': # this line is needed to avoid errors that occur on Windows computers

    parallelMultiCohort = P.ParallelMultiCohort(
        ids=range(N_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
        pop_sizes=[COHORT_POP_SIZE]*N_COHORTS,  # [COHORT_POP_SIZE, COHORT_POP_SIZE, ..., COHORT_POP_SIZE]
        mortality_probs=[MORTALITY_PROB]*N_COHORTS  # [p, p, ....]
    )

    parallelMultiCohort.simulate(TIME_STEPS)

    # plot the histogram of average survival time
    Fig.graph_histogram(
        data=parallelMultiCohort.multiCohortOutcomes.meanSurvivalTimes,
        title='Histogram of Mean Survival Time',
        x_label='Mean Survival Time (Year)',
        y_label='Count')

    # print projected mean survival time (years)
    print('Projected mean survival time (years)',
          parallelMultiCohort.multiCohortOutcomes.statMeanSurvivalTime.get_mean())

    # print projection interval
    print('95% projection (prediction, percentile, or uncertainty) interval of average survival time (years)',
          parallelMultiCohort.multiCohortOutcomes.statMeanSurvivalTime.get_PI(alpha=ALPHA))
