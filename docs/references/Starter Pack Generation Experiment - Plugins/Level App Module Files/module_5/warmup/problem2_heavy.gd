extends SequenceEvent

func trigger():
	var number_line = get_number_line()
	clear_number_line_labels(number_line)
	use_paint_tool(number_line._ticks[1])
	await delay(1)
	use_label_fraction_tool(number_line._ticks[1], true)
