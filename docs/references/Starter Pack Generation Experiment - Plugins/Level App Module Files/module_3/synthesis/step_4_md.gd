extends SequenceEvent

func trigger():
	for index in range(4):
		reset_shaded(get_frac_bar(index))