def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, withPole)


def moveDisk(fromPole, toPole):
    print("moving disk from", fromPole, "to", toPole)


moveTower(3, "A", "B", "C")
