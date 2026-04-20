extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_shaded_ticks(number_line)
