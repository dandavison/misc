from numpy.random import exponential
from numpy.random import uniform


def simulate_and_estimate(rate):
    number_of_sampled_event_streams = 100000
    times_to_first_event = exponential(scale=1 / rate, size=number_of_sampled_event_streams)
    print(
        f"(num_events)/(total_time) = %.3f"
        % (number_of_sampled_event_streams / times_to_first_event.sum())
    )
    print(
        f"mean(1/time) = %.3f"
        % ((1 / times_to_first_event).sum() / number_of_sampled_event_streams)
    )
    print(
        f"geometric_mean(1/time) = %.3f"
        % np.exp(np.log(1 / times_to_first_event).sum() / number_of_sampled_event_streams)
    )


def simulate_and_estimate_bounded(rate, time_bound, n):
    number_of_sampled_event_streams = int(n)
    all_times = exponential(scale=1 / rate, size=number_of_sampled_event_streams)
    times_to_first_event = all_times[all_times <= time_bound]
    n_T = len(times_to_first_event)
    n_B = len(all_times) - n_T
    rate_estimate = n_T / (times_to_first_event.sum() + time_bound * (n_B))
    print(f"n_T={n_T}, n_B={n_B}, rate_estimate={rate_estimate}")


def simulate_and_estimate_bounded_2(rate, n):
    number_of_sampled_event_streams = int(n)
    all_times = exponential(scale=1 / rate, size=number_of_sampled_event_streams)
    halfway_point = int(number_of_sampled_event_streams / 3)
    times_to_first_event = list(all_times[:halfway_point])
    potentially_bounded_times = list(all_times[halfway_point:])
    bounded_times = []
    for t in potentially_bounded_times:
        bound = uniform(1 / rate, 2 * 1 / rate)
        if t > bound:
            bounded_times.append(rate)
        else:
            times_to_first_event.append(t)
    n_T = len(times_to_first_event)
    n_B = len(bounded_times)
    rate_estimate = n_T / (sum(times_to_first_event) + sum(bounded_times))
    print(f"n_T={n_T}, n_B={n_B}, rate_estimate={rate_estimate}")


if __name__ == "__main__":
    simulate_and_estimate_bounded(rate=3.749)
