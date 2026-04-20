extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	number_line._ticks[1].is_read_only = true
