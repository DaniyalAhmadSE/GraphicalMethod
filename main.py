from models.equation import Equation
from models.line import Line
from models.point2d import Point2D as Point
from models.problem_model import ProblemModel
from models.term import Term


def solve(prob: ProblemModel):

    lines = [Line(Point(), Point())] * len(prob.const_eqs)

    points = [Point()] * 2

    for i, each_eq in enumerate(ProblemModel.const_eqs):
        for j, each_term in enumerate(each_eq.l_exp.terms):
            lines[i].points[j].coords[j] = each_eq.constant / each_term.coeff

    lines[0].Point2D_a = points[0]
    lines[0].Point2D_b = points[1]

    return


def main():
    # TODO: Implement Generically
    # n_constraints = int(input('No. of Constraints: '))

    xs = ['x1', 'x2', 'x3']
    prob_eq = Equation(
        [Term(10, xs[0]), Term(6, xs[1])],
        '=', const=0, is_z=True,
    )
    const_eqs = [
        Equation([Term(4, xs[0]), Term(5, xs[1])], '<=', 20),
        Equation([Term(4, xs[0]), Term(2, xs[1])], '>=', 6),
        Equation([Term(7, xs[0]), Term(0, xs[2])], '<=', 14),
    ]

    prob = ProblemModel(prob_eq, const_eqs)
    solve(prob)

    return None


if __name__ == "__main__":
    main()
