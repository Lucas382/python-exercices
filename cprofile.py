import cProfile
import pstats
import decrescente


def main():
    with cProfile.Profile() as pr:
        decrescente.main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    main()