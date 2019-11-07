from numpy.random import exponential

rate = 3.749
number_of_sampled_event_streams = 100000
times_to_first_event = exponential(scale=1 / rate, size=number_of_sampled_event_streams)
print(
    f"(num_events)/(total_time) = %.3f"
    % (number_of_sampled_event_streams / times_to_first_event.sum())
)
print(
    f"mean(1/time) = %.3f" % ((1 / times_to_first_event).sum() / number_of_sampled_event_streams)
)
print(
    f"geometric_mean(1/time) = %.3f"
    % np.exp(np.log(1 / times_to_first_event).sum() / number_of_sampled_event_streams)
)
