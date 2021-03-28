

import argparse, random

def simulate(num_doors, switch, verbose):
    """(int, bool): bool

    Carry out the game for one contestant.  If 'switch' is True,
    the contestant will switch their chosen door when offered the chance.
    Returns a Boolean value telling whether the simulated contestant won.
    """

    #3 doors, 0,1,2.

doorsremaining=3
doors=[0,1,2]
    # Randomly picks one of the doors to be correct.
winning_door = random.randint(0,2)
    

    # player than chooses door at random too.
PlayerChoice = random.randint(0,2);
print('player picked door', PlayerChoice)


doorsremaining = 2

    #monty shows one of the doors
Montydoor = random.randint(0,2)

removedoor=(Montydoor)

 # The host will never open the winning door, or the door chosen by the contestant.
if removedoor == winning_door or removedoor == PlayerChoice:
    (doorsremaining)

        # Remove the door from the list
doorsremaining2= doorsremaining- removedoor
    
    # Does the player want to switch?

def switch():
    switch = input("would you like to change your door you picked")
    if switch == ("Yes" or "Y"):
        PlayerChoice=doorsremaing

        # Change choice to the only door available.
        choice = available_doors.pop()
        if verbose:
            print('to {}'.format(choice+1))

    # Did the contestant win?
won = (PlayerChoice == winning_door)
if won:
    print('Contestant WON')

else:
            print('Contestant LOST')
           


def main():
    # Get command-line arguments, this is not all my own code
    parser = argparse.ArgumentParser(
        description='simulate')
    parser.add_argument('--doors', default=3, type=int, metavar='int',
                        help='number of doors offered to the contestant')
    parser.add_argument('--trials', default=1000, type=int, metavar='int',
                        help='number of trials to perform')
    parser.add_argument('--verbose', default=False, action='store_true',
                        help='display the results of each trial')
    args = parser.parse_args()

    print('Simulating {} trials...'.format(args.trials))

    # Carry out the trials
    winning_non_switchers = 0
    winning_switchers = 0
    for i in range(args.trials):
        # First, do a trial where the contestant never switches.
        won = simulate(args.doors, switch=False, verbose=args.verbose)
        if won:
            winning_non_switchers += 1

        # Next, try one where the contestant switches.
        won = simulate(args.doors, switch=True, verbose=args.verbose)
        if won:
            winning_switchers += 1

    print('    Switching won {0:5} times out of {1} ({2}% of the time)'.format(
            winning_switchers, args.trials,
            (winning_switchers / args.trials * 100 ) ))
    print('Not switching won {0:5} times out of {1} ({2}% of the time)'.format(
            winning_non_switchers, args.trials,
            (winning_non_switchers / args.trials * 100 ) ))


if __name__ == '__main__':
    main()
