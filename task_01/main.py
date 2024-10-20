import pulp


def solve(lims: dict[str, float]):
    model = pulp.LpProblem('Model', pulp.LpMaximize)

    x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    # Lemonade = 2 * water + 1 * sugar + 1 * juice
    x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')
    # FruitJuice = 1 * water + 2 * puree

    model += 2 * x1 + 1 * x2 <= lims['water'], 'WaterConstraint'
    model += 1 * x1 <= lims['sugar'], 'SugarConstraint'
    model += 1 * x1 <= lims['juice'], 'JuiceConstraint'
    model += 2 * x2 <= lims['puree'], 'PureeConstraint'
    model += x1 + x2, 'Goal'

    model.solve()
    return model, (x1, x2)


def main():
    lims = dict(
        water=100,
        sugar=50,
        juice=30,
        puree=40,
    )
    model, (x1, x2) = solve(lims=lims)

    print('================================')
    print(f'Status: {pulp.LpStatus[model.status]}')
    print(f'Water Used: {x1.varValue * 2 + x2.varValue} of {lims["water"]}')
    print(f'Sugar Used: {x1.varValue * 1} of {lims["sugar"]}')
    print(f'Juice Used: {x1.varValue * 1} of {lims["juice"]}')
    print(f'Puree Used: {x2.varValue * 2} of {lims["puree"]}')
    print('===========Products=============')
    print(f'{x1.name}: {x1.varValue}')
    print(f'{x2.name}: {x2.varValue}')
    print(f'Total Products: {x1.varValue + x2.varValue}')


if __name__ == '__main__':
    main()
