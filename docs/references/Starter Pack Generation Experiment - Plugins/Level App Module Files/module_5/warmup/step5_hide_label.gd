extends SequenceEvent

func trigger():
	var number_line = get_number_line(1)
	use_label_fraction_tool(number_line._ticks[1], false)
