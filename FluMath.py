# Calculating the percentage of population with influenza at any given point in time.
# Comparing this with the COVID data gives the likelihood that a patient displaying Flu-like
# symptoms has the Flu vs. COVID-19

# INPUT: provincePop <Integer>
# RETURNS: estimated population with flu per day for province <Integer>
def calcPopWithFlu(provincePop):

    # Percentage of the US population that has the flu on an average year, assuming Canadian proportion is the same
    # SOURCE:
    percentPopulationFluYear = .15

    # Flu season lasts on average from october to may: ~6 months
    # 6 * 30 = 180
    fluSeasonDays = 6 * 30  # days of flu season

    # Flu symptoms last an average of 5-7 days, so we get about 30 Flu cycles in a season.
    # 180 / 30 = 6
    fluCyclesSeason = 180 / 6

    # Dividing the percent of the population that will have the flu on in a year by the number of cycles
    # gives us the approximate percentage of the population that has the flu at any given point in time during
    # Flu season.  This calculation assumes even distribution across Flu season which is not reflected in real life,
    # with December/January having the peak.
    percentPopulationWithFluPerDay = percentPopulationFluYear / fluCyclesSeason  # = 0.005 or 0.5%

    popWithFluPerDay = provincePop * percentPopulationWithFluPerDay

    return popWithFluPerDay
