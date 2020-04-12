def estimator(data):
    # genearte impact report
    impact = generateImpact(data["reportedCases"], getNumberOfDays(
        data["periodType"], data["timeToElapse"]), data["totalHospitalBeds"],
        data["region"]["avgDailyIncomeInUSD"], data["region"]["avgDailyIncomePopulation"])

    # generate Severe impact report
    severeImpact = generateSevereImpact(data["reportedCases"], getNumberOfDays(
        data["periodType"], data["timeToElapse"]), data["totalHospitalBeds"],
        data["region"]["avgDailyIncomeInUSD"], data["region"]["avgDailyIncomePopulation"])

    return {"data": data, "impact": impact, "severeImpact": severeImpact}


def currentlyInfected(current, days):
    fac = int(days/3)
    infected = int(current * (2**fac))
    return infected


def availableBeds(severeCasesByRequestedTime, totalHospitalBeds):
    hospitalBedsByRequestedTime = int(
        (35/100 * totalHospitalBeds) - severeCasesByRequestedTime)
    return hospitalBedsByRequestedTime


def getNumberOfDays(periodType, timeSpan):
    if periodType == "days":
        return timeSpan

    elif periodType == "weeks":
        return timeSpan * 7

    elif periodType == "months":
        return timeSpan * 30
    return 0


def generateImpact(covid19Cases, timeInDays, hospitalBeds, avgIncome, avgIncomePopulation):
    impact = {}

    currentInfections = covid19Cases * 10

    infectionsByRequestedTime = currentlyInfected(
        currentInfections, timeInDays)

    severeCasesByRequestedTime = int(15/100 * infectionsByRequestedTime)

    hospitalBedsByRequestedTime = availableBeds(
        severeCasesByRequestedTime, hospitalBeds)

    casesForICUByRequestedTime = int(5/100 * infectionsByRequestedTime)

    casesForVentilatorsByRequestedTime = int(2/100 * infectionsByRequestedTime)

    dollarsInFlight = int((infectionsByRequestedTime *
                       avgIncomePopulation * avgIncome)/timeInDays)

    impact.update([("currentlyInfected", currentInfections),
                   ("infectionsByRequestedTime", infectionsByRequestedTime),
                   ("severeCasesByRequestedTime", severeCasesByRequestedTime),
                   ("hospitalBedsByRequestedTime", hospitalBedsByRequestedTime),
                   ("casesForICUByRequestedTime", casesForICUByRequestedTime),
                   ("casesForVentilatorsByRequestedTime",
                    casesForVentilatorsByRequestedTime),
                   ("dollarsInFlight", dollarsInFlight)])
    return impact


def generateSevereImpact(covid19Cases, timeInDays, hospitalBeds, avgIncome, avgIncomePopulation):
    severeImpact = {}

    currentInfections = covid19Cases * 50

    infectionsByRequestedTime = currentlyInfected(
        currentInfections, timeInDays)

    severeCasesByRequestedTime = int(15/100 * infectionsByRequestedTime)

    hospitalBedsByRequestedTime = availableBeds(
        severeCasesByRequestedTime, hospitalBeds)

    casesForICUByRequestedTime = int(5/100 * infectionsByRequestedTime)

    casesForVentilatorsByRequestedTime = int(2/100 * infectionsByRequestedTime)

    dollarsInFlight = int((infectionsByRequestedTime *
                       avgIncomePopulation * avgIncome)/timeInDays)

    severeImpact.update([("currentlyInfected", currentInfections),
                         ("infectionsByRequestedTime", infectionsByRequestedTime),
                         ("severeCasesByRequestedTime",
                          severeCasesByRequestedTime),
                         ("hospitalBedsByRequestedTime",
                          hospitalBedsByRequestedTime),
                         ("casesForICUByRequestedTime",
                          casesForICUByRequestedTime),
                         ("casesForVentilatorsByRequestedTime",
                          casesForVentilatorsByRequestedTime),
                         ("dollarsInFlight", dollarsInFlight)])

    return severeImpact


sample = {"region": {
    "name": "Africa",
    "avgAge": 19.7,
    "avgDailyIncomeInUSD": 5,
    "avgDailyIncomePopulation": 0.71
},
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}
